# Generated by Django 5.0.7 on 2024-08-18 09:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0038_tweet_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usera',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]