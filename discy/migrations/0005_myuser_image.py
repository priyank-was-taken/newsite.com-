# Generated by Django 4.0.4 on 2022-05-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discy', '0004_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='discy/image'),
        ),
    ]
