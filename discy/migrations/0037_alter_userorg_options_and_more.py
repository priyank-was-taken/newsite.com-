# Generated by Django 4.0.5 on 2022-08-17 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0036_alter_userorg_employee_alter_userorg_organisation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userorg',
            options={'verbose_name': 'UserOrg', 'verbose_name_plural': 'UserOrg'},
        ),
        migrations.RenameField(
            model_name='organisation',
            old_name='organisation',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userorg',
            old_name='organisation',
            new_name='name',
        ),
    ]