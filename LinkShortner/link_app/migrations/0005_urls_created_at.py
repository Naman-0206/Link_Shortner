# Generated by Django 4.2.1 on 2023-05-25 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link_app', '0004_alter_urls_ids'),
    ]

    operations = [
        migrations.AddField(
            model_name='urls',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 25, 13, 51, 1, 314491)),
        ),
    ]
