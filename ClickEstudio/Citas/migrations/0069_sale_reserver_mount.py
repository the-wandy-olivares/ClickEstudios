# Generated by Django 5.0 on 2024-10-25 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0068_rename_reserve_sale_reserver'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='reserver_mount',
            field=models.IntegerField(blank=True, default=500, null=True),
        ),
    ]
