# Generated by Django 3.1.5 on 2024-04-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0014_auto_20240411_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('NEW', 'NEW')], default='PRESENT', max_length=50),
        ),
    ]
