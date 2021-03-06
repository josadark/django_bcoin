# Generated by Django 3.2 on 2021-06-14 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0008_alter_stock_marketcap'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='SMA2000',
        ),
        migrations.AddField(
            model_name='stock',
            name='SMA200',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stock',
            name='ATR',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='EPSnext5year',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='EPSnextyear',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='EPSpast5year',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='EPSthisyear',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='Gap',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='SMA20',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='SMA50',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='beta',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='change',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='dividend',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='float',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='floatshort',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='fromopen',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='grossm',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='high52',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='insiderOwn',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='insiderTrans',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='instOwn',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='instTrans',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='low52',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='operm',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='outstanding',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfhalf',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfmonth',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfquart',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfweek',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfyear',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='perfytd',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='profit',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='returnonassets',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='returnonequity',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='returnoninvestment',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volatilitym',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='stock',
            name='volatilityw',
            field=models.CharField(max_length=8),
        ),
    ]
