# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_service', '0003_auto_20150406_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entities'),
        ),
        migrations.AlterField(
            model_name='picture',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entities'),
        ),
        migrations.AlterField(
            model_name='story',
            name='liked_entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, default=b'', blank=True, to='rest_service.LikedEntity', null=True, verbose_name=b'Entities'),
        ),
    ]
