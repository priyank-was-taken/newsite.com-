# Generated by Django 4.0.5 on 2022-08-17 11:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0041_rename_name_userorg_organisation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorg',
            name='organisation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='discy.organisation', unique=True),
        ),
        migrations.AlterField(
            model_name='userorg',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
