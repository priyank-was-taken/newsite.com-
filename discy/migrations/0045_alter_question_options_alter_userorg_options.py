# Generated by Django 4.0.5 on 2022-08-18 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0044_alter_userorg_organisation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterModelOptions(
            name='userorg',
            options={'verbose_name': 'UserOrg', 'verbose_name_plural': 'UserOrges'},
        ),
    ]
