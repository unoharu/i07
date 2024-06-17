from django.db import models
from django.utils.translation import gettext_lazy as _

class Table(models.Model):
    max_seats = models.IntegerField(
        max_length=2,
        unique=False,
        verbose_name=_("max_seats")
        )
    status = models.CharField(
        max_length=50,
        unique=False,
        verbose_name=_("status")
        )
    
    class Meta:
        db_table = 'table'

    def __str__(self):
        return f'Table {self.id}'