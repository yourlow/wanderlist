# Generated by Django 3.0.4 on 2020-10-10 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderlist', '0004_activity_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='imageurl',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
