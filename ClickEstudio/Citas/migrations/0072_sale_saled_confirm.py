# Generated by Django 5.0 on 2024-10-25 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0071_sale_abonado'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='saled_confirm',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
