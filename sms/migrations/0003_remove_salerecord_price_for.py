# Generated by Django 2.1.3 on 2019-02-06 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20190206_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salerecord',
            name='price_for',
        ),
    ]
