# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150616_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
