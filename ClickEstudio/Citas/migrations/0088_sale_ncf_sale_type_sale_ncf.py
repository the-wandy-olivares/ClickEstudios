# Generated by Django 5.0 on 2024-12-08 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0087_company_logo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='ncf',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='sale',
            name='type_sale_ncf',
            field=models.BooleanField(default=False),
        ),
    ]