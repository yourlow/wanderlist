# Generated by Django 3.1.1 on 2020-10-20 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wanderlist', '0008_auto_20201019_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='decription',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='guidance_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='sustainable_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]