# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('completed', '-created_at')},
        ),
        migrations.AlterField(
            model_name='todo',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
