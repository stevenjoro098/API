# Generated by Django 2.2 on 2019-05-09 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsRoom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsroom',
            name='slug',
            field=models.SlugField(default='Event', unique=True),
        ),
    ]