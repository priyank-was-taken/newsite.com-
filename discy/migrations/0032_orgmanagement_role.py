# Generated by Django 4.0.5 on 2022-08-17 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0031_delete_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='orgmanagement',
            name='role',
            field=models.CharField(choices=[('DVP', 'developer'), ('TST', 'tester'), ('QA', 'quality assurance'), ('MGR', 'manager'), ('TL', 'team leader')], max_length=30, null=True),
        ),
    ]
