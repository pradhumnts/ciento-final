# Generated by Django 3.1.7 on 2021-10-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecondAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('approve_ambassador_affiliate', models.BooleanField()),
                ('see_reports', models.BooleanField()),
                ('get_notifications', models.BooleanField()),
            ],
        ),
    ]
