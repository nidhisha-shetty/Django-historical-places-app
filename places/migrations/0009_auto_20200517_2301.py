# Generated by Django 2.2.4 on 2020-05-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20200517_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='places',
            name='place_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
