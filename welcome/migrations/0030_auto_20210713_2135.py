# Generated by Django 3.2 on 2021-07-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0029_auto_20210713_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicstockasset',
            name='value',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='publicstockasset',
            name='volume',
            field=models.IntegerField(default=0.0),
        ),
    ]
