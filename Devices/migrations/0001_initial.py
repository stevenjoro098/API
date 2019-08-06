# Generated by Django 2.2 on 2019-05-01 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=250)),
                ('device_slug', models.SlugField(max_length=250, unique=True)),
                ('token_value', models.CharField(blank=True, max_length=250)),
                ('device_status', models.BooleanField(default=False)),
                ('longitude', models.FloatField(max_length=250)),
                ('latitude', models.FloatField(max_length=250)),
            ],
        ),
    ]