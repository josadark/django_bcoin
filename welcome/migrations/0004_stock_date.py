# Generated by Django 3.2 on 2021-06-01 20:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0003_auto_20210526_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
