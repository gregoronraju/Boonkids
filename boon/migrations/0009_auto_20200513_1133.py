# Generated by Django 3.0.4 on 2020-05-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0008_auto_20200513_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxcategory',
            name='categoryType',
            field=models.CharField(max_length=50),
        ),
    ]