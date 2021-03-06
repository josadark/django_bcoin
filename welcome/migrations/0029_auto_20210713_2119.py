# Generated by Django 3.2 on 2021-07-14 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0028_publicportfolio_publicstockasset'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicstockasset',
            name='buyPrice',
        ),
        migrations.RemoveField(
            model_name='publicstockasset',
            name='change',
        ),
        migrations.RemoveField(
            model_name='publicstockasset',
            name='date_purchased',
        ),
        migrations.RemoveField(
            model_name='publicstockasset',
            name='earnings',
        ),
        migrations.RemoveField(
            model_name='publicstockasset',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='publicstockasset',
            name='value',
        ),
        migrations.AlterField(
            model_name='publicstockasset',
            name='portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='welcome.publicportfolio'),
        ),
    ]
