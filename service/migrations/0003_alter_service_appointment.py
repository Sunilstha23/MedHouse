# Generated by Django 3.2.5 on 2021-07-23 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20210714_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='appointment',
            field=models.CharField(max_length=100),
        ),
    ]
