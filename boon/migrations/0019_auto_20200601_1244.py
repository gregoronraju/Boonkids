# Generated by Django 3.0.4 on 2020-06-01 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0018_auto_20200519_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salesvoucher',
            old_name='netBalance',
            new_name='netAmount',
        ),
    ]
