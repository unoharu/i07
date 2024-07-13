from django.db import models
from table.models import Table
from django.utils.translation import gettext_lazy as _

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    people = models.IntegerField(null=True, blank=True, verbose_name=_("people"))
    date = models.DateField(null=True, blank=True, verbose_name=_("date"))
    check_in_time = models.TimeField(null=True, blank=True, auto_now_add=True, verbose_name=_("check_in_time"))
    check_out_time = models.TimeField(null=True, blank=True, verbose_name=_("check_out_time"))
    stay_time = models.TimeField(null=True, blank=True, verbose_name=_("stay_time"))
    
    table_id = models.ForeignKey(Table, verbose_name=_("table_id"), on_delete=models.CASCADE)

    class Meta:
        db_table = 'customer'
    
    def __str__(self):
        return f'Customer {self.id}'

    @classmethod
    def get_next_group_id(cls):
        last_customer = cls.objects.all().order_by('id').last()
        if not last_customer:
            return 1
        return last_customer.id + 1