# Generated by Django 3.2 on 2021-07-21 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0034_screenasset'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='maxChange',
            field=models.FloatField(default=300.0),
        ),
        migrations.AddField(
            model_name='screen',
            name='maxRelativeVolume',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='screen',
            name='maxShortRatio',
            field=models.FloatField(default=100),
        ),
        migrations.AddField(
            model_name='screen',
            name='minChange',
            field=models.FloatField(default=-300.0),
        ),
        migrations.AddField(
            model_name='screen',
            name='minRelativeVolume',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='screen',
            name='minShortRatio',
            field=models.FloatField(default=0),
        ),
    ]
