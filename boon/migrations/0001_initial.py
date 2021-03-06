# Generated by Django 2.2.5 on 2020-03-19 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brandmaster',
            fields=[
                ('brandId', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Categorymaster',
            fields=[
                ('sno', models.AutoField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('barcodeId', models.IntegerField()),
                ('productName', models.CharField(max_length=50)),
                ('productdescription', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('measurements', models.DecimalField(decimal_places=4, max_digits=10)),
                ('unitRate', models.DecimalField(decimal_places=4, max_digits=10)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boon.Brandmaster')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boon.Categorymaster')),
            ],
        ),
        migrations.CreateModel(
            name='Supplierdetails',
            fields=[
                ('supplierid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('suppliername', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phonenumber', models.DecimalField(decimal_places=0, max_digits=15)),
                ('mobile', models.DecimalField(decimal_places=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantityOnHand', models.DecimalField(decimal_places=0, max_digits=15)),
                ('purchaseDate', models.DateField()),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boon.Product')),
            ],
        ),
        migrations.CreateModel(
            name='Materialpurchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boon.Product')),
                ('suppilerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boon.Supplierdetails')),
            ],
        ),
    ]
