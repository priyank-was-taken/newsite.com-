# Generated by Django 4.0.5 on 2022-08-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0021_alter_organisation_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(default='', max_length=30)),
            ],
            options={
                'verbose_name': 'Role',
                'verbose_name_plural': 'Roles',
            },
        ),
        migrations.AlterModelOptions(
            name='organisation',
            options={'verbose_name': 'Organisation', 'verbose_name_plural': 'Organisations'},
        ),
    ]