from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Table

# Create your views here.
class TableView(TemplateView):
    template_name = 'table/layout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tables'] = Table.objects.all()
        return context
