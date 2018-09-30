# Generated by Django 2.0.6 on 2018-07-29 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cornerstone', '0006_child_on_trip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='unpicked_kids',
        ),
        migrations.AddField(
            model_name='trip',
            name='absent_kids',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_kids',
            field=models.ManyToManyField(to='cornerstone.Child'),
        ),
    ]
