# Generated by Django 3.0.7 on 2021-02-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20210221_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='country',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
