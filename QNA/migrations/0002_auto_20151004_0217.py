# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QNA', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appeared',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='appeared_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='appeared_marks',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='asked_by',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.DeleteModel(
            name='Appeared',
        ),
    ]
