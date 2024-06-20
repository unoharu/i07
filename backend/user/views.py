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
            date = timezone.now().date()
            check_in_time = timezone.now().time()
            people = form.cleaned_data['people']

            # statusが'o'のテーブルをmax_seats昇順で取得
            available_tables = Table.objects.filter(status='o').order_by('max_seats')
            if not available_tables.exists():
                messages.error(request, '利用可能なテーブルがありません。')
                return redirect('user:add_customers')

            remaining_customers = people
            selected_tables = []
            
            for table in available_tables:
                if remaining_customers <= 0:
                    break
                selected_tables.append(table)
                remaining_customers -= table.max_seats

            if remaining_customers > 0:
                messages.error(request, '十分な席数がありません。')
                return redirect('user:add_customers')

            # 最初のテーブルにCustomerレコードを作成
            customer = Customer.objects.create(
                people=people,
                date=date,
                check_in_time=check_in_time,
                table_id=selected_tables[0]  # 最初のテーブルを割り当てて保存
            )

            # 他のテーブルを割り当ててステータスを更新
            selected_tables[len(selected_tables) - 1].status = 'x'
            table.save()

            messages.success(request, '顧客が正常に追加されました。')
            return redirect(reverse('user:success_url', kwargs={'group_id': customer.id}))
    else:
        form = CustomerGroupForm()
    
    return render(request, 'user/add_customers.html', {'form': form})

def success_view(request, group_id):
    return render(request, 'user/success.html', {'group_id': group_id})