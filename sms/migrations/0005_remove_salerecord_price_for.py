# Generated by Django 2.1.3 on 2019-02-07 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0004_salerecord_price_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salerecord',
            name='price_for',
        ),
    ]
