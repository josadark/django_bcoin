# Generated by Django 3.2 on 2021-06-30 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0023_chinastock'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='value',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockasset',
            name='buyPrice',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
