from django.shortcuts import render,  redirect
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, CreateView, TemplateView
from django.contrib import messages
from .forms import CustomerGroupForm
from .models import Customer
from table.models import Table

# Create your views here.

class ReceptionView(TemplateView):
    template_name = 'user/reception.html'


def add_customers(request):
    if request.method == "POST":
        form = CustomerGroupForm(request.POST)
        if form.is_valid():
            group_id = Customer.get_next_group_id()  # 自動インクリメントされたgroup_idを取得
            date = timezone.now().date()
            check_in_time = timezone.now().time()
            number_of_customers = form.cleaned_data['number_of_customers']

            # statusが'o'のテーブルをID順に取得
            available_tables = Table.objects.filter(status='o').order_by('id')
            if not available_tables.exists():
                messages.error(request, '利用可能なテーブルがありません。')
                return redirect('user:add_customers')

            total_seats = 0
            selected_tables = []
            for table in available_tables:
                selected_tables.append(table)
                total_seats += table.max_seats
                if total_seats >= number_of_customers:
                    break

            if total_seats < number_of_customers:
                messages.error(request, '十分な席数がありません。')
                return redirect('user:add_customers')

            remaining_customers = number_of_customers
            for table in selected_tables:
                seats_to_fill = min(remaining_customers, table.max_seats)
                for _ in range(seats_to_fill):
                    Customer.objects.create(
                        group_id=group_id,
                        date=date,
                        check_in_time=check_in_time,
                        table_id=table
                    )
                remaining_customers -= seats_to_fill
                table.status = 'x'
                table.save()

            messages.success(request, '顧客が正常に追加されました。')
            return redirect(reverse('user:success_url', kwargs={'group_id': group_id}))
    else:
        form = CustomerGroupForm()
    
    return render(request, 'user/add_customers.html', {'form': form})

def success_view(request, group_id):
    return render(request, 'user/success.html', {'group_id': group_id})