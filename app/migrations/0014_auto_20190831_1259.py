# Generated by Django 2.2.4 on 2019-08-31 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190830_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='available',
            field=models.BooleanField(),
        ),
    ]
