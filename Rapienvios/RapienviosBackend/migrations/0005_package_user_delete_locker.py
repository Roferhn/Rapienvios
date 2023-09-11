# Generated by Django 4.2.4 on 2023-09-07 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RapienviosBackend', '0004_rename_package_id_locker_package_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RapienviosBackend.user'),
        ),
        migrations.DeleteModel(
            name='Locker',
        ),
    ]