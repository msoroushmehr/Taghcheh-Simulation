# Generated by Django 4.0.3 on 2022-03-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0051_category_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='hits',
        ),
        migrations.AddField(
            model_name='book',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='myapp.myipaddress', verbose_name='بازدیدها'),
        ),
    ]
