# Generated by Django 2.2.3 on 2019-08-16 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nlmkapp', '0008_auto_20190816_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voipgw',
            name='voip_ip',
            field=models.CharField(max_length=20, verbose_name='Ip voip gw'),
        ),
    ]