# Generated by Django 3.0.4 on 2020-05-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0009_auto_20200513_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxcategory',
            name='tax',
        ),
        migrations.AddField(
            model_name='taxcategory',
            name='tax',
            field=models.ManyToManyField(max_length=50, to='boon.Tax'),
        ),
    ]
