# Generated by Django 4.0.5 on 2022-08-17 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0017_alter_employee_manager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='org_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
