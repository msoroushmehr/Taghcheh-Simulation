# Generated by Django 4.0.3 on 2022-03-19 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0056_bookhit_book_hits_bookhit_book_bookhit_ip_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='special_user',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='کابرویژه تا'),
        ),
    ]
