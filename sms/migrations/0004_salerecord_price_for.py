# Generated by Django 2.1.3 on 2019-02-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0003_remove_salerecord_price_for'),
    ]

    operations = [
        migrations.AddField(
            model_name='salerecord',
            name='price_for',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=10),
            preserve_default=False,
        ),
    ]
