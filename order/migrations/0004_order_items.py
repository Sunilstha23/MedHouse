# Generated by Django 3.2.5 on 2021-07-24 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]