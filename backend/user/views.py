from django.shortcuts import render,  redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from django.contrib import messages
from .forms import CustomerGroupForm
from .models import Customer
from table.models import Table
from django.db import transaction

class ReceptionView(TemplateView):
    template_name = 'user/reception.html'


def add_customers(request):
    if request.method == "POST":
        form = CustomerGroupForm(request.POST)
        if form.is_valid():
            date = timezone.now().date()
            check_in_time = timezone.now().time()
            people = form.cleaned_data['people']

            available_tables = Table.objects.filter(status='o').order_by('max_seats')
            if not available_tables.exists():
                messages.error(request, '利用可能なテーブルがありません。')
                return redirect('user:add_customers')

            remaining_customers = people
            selected_tables = []
            
            def get_table_for_customers(num):
                table = available_tables.filter(max_seats=num).first()
                if table:
                    available_tables.filter(id=table.id).update(status='x')
                    return table
                return None

            # 優先される席
            table_map = {
                1: [1],
                2: [2],
                3: [4],
                4: [4],
                5: [10],
                6: [10],
                7: [10],
                8: [10],
                9: [10],
                10: [10]
            }
            
            while remaining_customers > 0:
                table_size_options = table_map.get(remaining_customers, [])
                if not table_size_options:
                    table_size_options = [10]  # Default to 10 if no specific size found

                table_found = False
                for size in table_size_options:
                    table = get_table_for_customers(size)
                    if table:
                        selected_tables.append(table)
                        remaining_customers -= table.max_seats
                        table_found = True
                        break

                if not table_found:
                    next_smaller_size = remaining_customers // 2
                    for size in range(next_smaller_size, 0, -1):
                        table = get_table_for_customers(size)
                        if table:
                            selected_tables.append(table)
                            remaining_customers -= table.max_seats
                            table_found = True
                            break

                if not table_found:
                    messages.error(request, '十分な席数がありません。')
                    return redirect('user:add_customers')

            try:
                with transaction.atomic():
                    for table in selected_tables:
                        Customer.objects.create(
                            people=min(table.max_seats, people),
                            date=date,
                            check_in_time=check_in_time,
                            table_id=table
                        )

                    messages.success(request, '顧客が正常に追加されました。')
                    return redirect(reverse('user:success_url', kwargs={'group_id': selected_tables[0].id}))

            except Exception as e:
                messages.error(request, f'エラーが発生しました: {str(e)}')
                return redirect('user:add_customers')

    else:
        form = CustomerGroupForm()

    return render(request, 'user/add_customers.html', {'form': form})

def success_view(request, group_id):
    return render(request, 'user/success.html', {'group_id': group_id})