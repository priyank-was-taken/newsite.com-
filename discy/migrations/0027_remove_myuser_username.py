# Generated by Django 4.0.5 on 2022-08-17 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0026_myuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='username',
        ),
    ]
