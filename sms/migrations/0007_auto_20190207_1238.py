# Generated by Django 2.1.3 on 2019-02-07 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0006_salerecord_price_for'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salerecord',
            old_name='price_for',
            new_name='total_amount_collected',
        ),
    ]
