# Generated by Django 3.0.4 on 2020-05-13 06:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0007_auto_20200513_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='taxcategory',
            old_name='shortCode',
            new_name='categoryType',
        ),
    ]