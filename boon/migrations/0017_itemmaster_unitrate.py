# Generated by Django 3.0.4 on 2020-05-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boon', '0016_auto_20200514_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmaster',
            name='unitRate',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=10),
            preserve_default=False,
        ),
    ]
