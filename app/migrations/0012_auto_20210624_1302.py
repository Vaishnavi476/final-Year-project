# Generated by Django 3.1.7 on 2021-06-24 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20210624_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='durations',
            field=models.CharField(choices=[('1', '1-Day'), ('2', '2-Day'), ('3', '3-Day'), ('4', '4-Day'), ('5', '5-Day'), ('6', '6-Day'), ('7', '7-Day'), ('8', '8-Day'), ('9', '9-Day'), ('10', '10-Day')], max_length=100),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='hr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hr_person', to='app.human_resource'),
        ),
    ]
