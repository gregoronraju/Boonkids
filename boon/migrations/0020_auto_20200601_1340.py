# Generated by Django 3.0.4 on 2020-06-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0019_auto_20200601_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesvoucher',
            name='address',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='recieved',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='reference',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='rounding',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salesvoucher',
            name='tin',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]