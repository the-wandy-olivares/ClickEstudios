# Generated by Django 5.0.6 on 2024-06-26 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Citas', '0030_alter_role_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='img',
        ),
        migrations.AddField(
            model_name='usera',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
