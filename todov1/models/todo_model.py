from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING

# Create your models here.
class Todo(models.Model):
    todo = models.TextField(verbose_name='Todos')
    addt = models.TextField(verbose_name="Additional data", null=True)
    created_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Username", on_delete=DO_NOTHING) # donothing

