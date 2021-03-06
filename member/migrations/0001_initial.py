# Generated by Django 3.1.7 on 2021-10-24 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ambassador', '0001_initial'),
        ('affiliate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('lastName', models.CharField(max_length=60)),
                ('nickName', models.CharField(max_length=60)),
                ('profile', models.URLField(blank=True, null=True)),
                ('number', models.IntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=40)),
                ('dob', models.DateField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=100)),
                ('photo_id', models.URLField(blank=True, null=True)),
                ('affiliates', models.ManyToManyField(blank=True, related_name='members_affiliate', to='affiliate.Affiliate')),
                ('memberships', models.ManyToManyField(blank=True, related_name='members_membership', to='ambassador.Membership')),
            ],
        ),
    ]
