# Generated by Django 3.1.1 on 2020-10-20 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderlist', '0009_auto_20201021_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='decription',
        ),
        migrations.AlterField(
            model_name='activity',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
