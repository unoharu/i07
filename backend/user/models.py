from django.db import models
from table.models import Table
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    group_id = models.IntegerField()
    date = models.DateField(null=True, blank=True, verbose_name=_("date"))
    check_in_time = models.TimeField(null=True, blank=True, auto_now_add=True, verbose_name=_("check_in_time"))
    check_out_time = models.TimeField(null=True, blank=True, auto_now=True, verbose_name=_("check_out_time"))
    age = models.IntegerField(null=True, blank=True, verbose_name=_("age"))
    gender = models.CharField(max_length=10, null=True, blank=True, verbose_name=_("gender"))
    table_id = models.ForeignKey(Table, verbose_name=_("table_id"), on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'
    
    def __str__(self):
        return f'Customer {self.group_id}'

    @classmethod
    def get_next_group_id(cls):
        last_customer = cls.objects.all().order_by('group_id').last()
        if not last_customer:
            return 1
        return last_customer.group_id + 1