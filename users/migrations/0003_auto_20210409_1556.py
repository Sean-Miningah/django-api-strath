# Generated by Django 3.1.7 on 2021-04-09 12:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210409_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 9, 15, 56, 30, 124541)),
        ),
    ]
