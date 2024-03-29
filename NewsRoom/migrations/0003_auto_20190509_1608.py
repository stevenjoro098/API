# Generated by Django 2.2 on 2019-05-09 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsRoom', '0002_newsroom_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsroom',
            name='venue',
            field=models.CharField(default='Nairobi', max_length=250),
        ),
        migrations.AlterField(
            model_name='newsroom',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
