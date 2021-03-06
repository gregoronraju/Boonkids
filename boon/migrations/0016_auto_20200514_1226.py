# Generated by Django 3.0.4 on 2020-05-14 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0015_auto_20200514_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucheritem',
            name='brand',
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='voucheritem',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
        migrations.AlterField(
            model_name='voucheritem',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='voucheritem',
            name='tax',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=10),
        ),
    ]
