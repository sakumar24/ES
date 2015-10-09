# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(max_length=1500)),
                ('views', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('answerd_by', models.CharField(max_length=20)),
                ('answerd_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Appeared',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('appeared_date', models.DateField()),
                ('appeared_marks', models.FloatField()),
            ],
            options={
                'ordering': ('appeared_date', 'appeared_marks'),
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(max_length=500)),
                ('course_name', models.CharField(max_length=80)),
                ('views', models.IntegerField(default=0)),
                ('important_votes', models.IntegerField(default=0)),
                ('asked_by', models.CharField(max_length=20)),
                ('posted_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('course_name',),
            },
        ),
        migrations.AddField(
            model_name='appeared',
            name='question',
            field=models.ManyToManyField(to='QNA.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='QNA.Question'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='answer',
            order_with_respect_to='question',
        ),
    ]
