# Generated by Django 2.1.5 on 2020-10-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20201017_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='altitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.FloatField(),
        ),
    ]
