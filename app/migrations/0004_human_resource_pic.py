# Generated by Django 3.1.7 on 2021-06-08 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_human_resource_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='human_resource',
            name='pic',
            field=models.ImageField(default='hr.png', upload_to='hr'),
        ),
    ]
