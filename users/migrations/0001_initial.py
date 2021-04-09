# Generated by Django 3.1.7 on 2021-04-09 10:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=100, unique=True)),
                ('active', models.BooleanField(null=True)),
                ('profile_image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('OTHER', 'other')], max_length=20)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('firebase_uid', models.CharField(blank=True, max_length=100, verbose_name='firebase User ID')),
                ('date_created', models.DateTimeField(default=datetime.datetime(2021, 4, 9, 13, 34, 27, 368325))),
                ('bio', models.TextField(max_length=400)),
                ('isVendor', models.BooleanField(null=True)),
                ('isVerified', models.BooleanField(null=True)),
                ('followers', models.IntegerField(null=True)),
                ('following', models.IntegerField(null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
