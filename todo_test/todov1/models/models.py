from django.db import models

# Create your models here.
class Todos(models.Model):
    todo = models.TextField(verbose_name='Todos')
    addt = models.TextField(verbose_name="Additional data",null=True)
    created_date = models.DateField(auto_now=True)

