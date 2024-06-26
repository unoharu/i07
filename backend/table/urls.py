from django.urls import path
from .views import TableView

app_name = 'table'

urlpatterns = [
    path('table/', TableView.as_view(), name="table"),
]