from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE  

# Create your models here.
class Todos(models.Model):
    todo = models.TextField(verbose_name='Todos')
    addt = models.TextField(verbose_name="Additional data",null=True)
    created_date = models.DateField(auto_now=True)
    user = models.ForeignKey(User, verbose_name="Username",on_delete=CASCADE)
