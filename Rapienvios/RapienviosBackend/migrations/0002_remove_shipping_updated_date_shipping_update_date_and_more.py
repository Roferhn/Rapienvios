# Generated by Django 4.2.4 on 2023-09-04 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RapienviosBackend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shipping',
            name='updated_date',
        ),
        migrations.AddField(
            model_name='shipping',
            name='update_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='packaged_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='shipping_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='RapienviosBackend.shipping'),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='delivery_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='shipping_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
