# Generated by Django 3.0.5 on 2020-08-21 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
