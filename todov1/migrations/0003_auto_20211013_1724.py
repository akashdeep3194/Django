# Generated by Django 3.2.5 on 2021-10-13 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todov1', '0002_alter_person_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.TextField(null=True, verbose_name='Todos')),
                ('created_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
