# Generated by Django 3.1.7 on 2021-04-09 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Channels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 16, 17, 5, 732242)),
        ),
        migrations.AlterField(
            model_name='channelsubscribertracker',
            name='date_subscribed',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 16, 17, 5, 732242)),
        ),
    ]