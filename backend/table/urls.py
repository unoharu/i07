from django.urls import path
from .views import TableView, update_status

app_name = 'table'

urlpatterns = [
    path('table/', TableView.as_view(), name="table"),
    path('update_status/', update_status, name='update_status'),
]