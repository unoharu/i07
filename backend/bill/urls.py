from django.urls import path
from . import views

app_name = 'bill'

urlpatterns = [
    path('update_status/', views.update_status, name='update_status'),
    path('success/', views.SuccessView.as_view(), name='success_url'), 
]