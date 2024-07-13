from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import TemplateView
from .models import Table
from user.models import Customer
from .forms import TableIDForm
from user.models import Customer
from django.utils import timezone

# Create your views here.
class TableView(TemplateView):
    template_name = 'table/layout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.all()
        context['users'] = Customer.objects.all().filter(check_out_time__isnull=True)
        return context

def update_status(request):
    if request.method == 'POST':
        table_id = request.POST.get('table_id')
        if table_id:
            try:
                table_id = int(table_id)  # table_idを整数に変換
            except ValueError:
                return JsonResponse({'success': False, 'errors': 'Invalid table_id'})

            table = get_object_or_404(Table, id=table_id)
            table.status = 'o'  # 状態を更新
            table.save()
            
            customer = Customer.objects.filter(check_out_time__isnull=True, table_id=table_id).first()
            if customer:
                customer.check_out_time = timezone.now()  # 現在の日時をcheckout_timeに設定
                customer.save()

            return JsonResponse({'success': True, 'table_id': table_id})
        else:
            return JsonResponse({'success': False, 'errors': 'table_id is required'})
    
    tables = Table.objects.all()  # テーブルデータをテンプレートに渡す
    return render(request, 'table/table.html', {'tables': tables})