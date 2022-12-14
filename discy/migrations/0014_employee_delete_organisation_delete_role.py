# Generated by Django 4.0.5 on 2022-08-17 03:22

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0013_role_alter_organisation_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('role', models.CharField(choices=[('STD', 'base employee'), ('MGR', 'manager'), ('SRMGR', 'senior manager'), ('PRES', 'president')], max_length=25)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='discy.employee')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Organisation',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
