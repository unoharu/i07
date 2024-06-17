from django.urls import path
from .views import ReceptionView, add_customers, success_view

app_name = 'user'

urlpatterns = [
    path('reception/', ReceptionView.as_view(), name="reception"),
    path('add_customers/', add_customers, name="add_customers"),
    path('success/<int:group_id>/', success_view, name='success_url'), 
]