# Generated by Django 2.2.4 on 2019-08-30 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190830_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
