# Generated by Django 3.2.5 on 2021-10-19 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todov1', '0005_alter_todos_todo'),
    ]

    operations = [
        migrations.AddField(
            model_name='todos',
            name='created_by',
            field=models.TextField(default='test', verbose_name='Username'),
            preserve_default=False,
        ),
    ]
