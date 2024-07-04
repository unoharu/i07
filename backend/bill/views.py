from django.shortcuts import render, redirect, get_object_or_404
from table.models import Table
from .forms import TableIDForm
from django.views.generic import DetailView, ListView, CreateView, TemplateView

def update_status(request):
    if request.method == 'POST':
        form = TableIDForm(request.POST)
        if form.is_valid():
            table_id = form.cleaned_data['table_id']
            table = get_object_or_404(Table, id=table_id)
            table.status = 'o'  # 状態を更新
            table.save()
            return redirect('bill:success_url')  # 更新後にリダイレクトするURLを指定
    else:
        form = TableIDForm()
    
    return render(request, 'bill/update_status.html', {'form': form})

class SuccessView(TemplateView):
    template_name = 'bill/success.html'
