# Generated by Django 4.2.4 on 2023-09-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RapienviosBackend', '0002_remove_shipping_updated_date_shipping_update_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricing',
            name='final_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
