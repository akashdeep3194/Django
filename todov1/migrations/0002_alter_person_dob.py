# Generated by Django 3.2.5 on 2021-10-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todov1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='DOB',
            field=models.DateField(auto_created=True),
        ),
    ]
