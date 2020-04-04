# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('card_content', '0002_auto_20200404_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(max_length=100, default=datetime.datetime(2020, 4, 4, 19, 20, 24, 111372, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
