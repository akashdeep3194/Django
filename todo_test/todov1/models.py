from django.db import models

# Create your models here.
class Todos(models.Model):
    todo = models.TextField(verbose_name='Todos',null = True)
    created_date = models.DateField(auto_now=True)
