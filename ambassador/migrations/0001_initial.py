# Generated by Django 3.1.7 on 2021-10-24 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambassador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('profile', models.URLField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=40)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SecondAmbassador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('profile', models.URLField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=40)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('add_ambassador', models.BooleanField()),
                ('change_offers', models.BooleanField()),
                ('see_reports', models.BooleanField()),
                ('invite_members', models.BooleanField()),
                ('get_notifications', models.BooleanField()),
                ('ambassador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambassador.ambassador')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_till', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('require_photo_id', models.BooleanField()),
                ('ambassador_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambassador.ambassador')),
            ],
        ),
    ]