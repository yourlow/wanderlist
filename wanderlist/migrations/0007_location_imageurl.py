# Generated by Django 3.0.4 on 2020-10-16 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderlist', '0006_auto_20201010_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='imageurl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
