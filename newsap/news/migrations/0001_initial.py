# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 10:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='map_unresolved_resolved_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='map_unresolved_resolved_news_type_map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='resolved_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolved_location_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='resolved_news_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolved_news_type_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=250)),
                ('source_url', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='unresolved_location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unresolved_location_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='unresolved_news_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unresolved_news_type_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='map_unresolved_resolved_news_type_map',
            name='resolved_news_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.resolved_news_type'),
        ),
        migrations.AddField(
            model_name='map_unresolved_resolved_news_type_map',
            name='unresolved_news_type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.unresolved_news_type'),
        ),
        migrations.AddField(
            model_name='map_unresolved_resolved_location',
            name='resolved_location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.resolved_location'),
        ),
        migrations.AddField(
            model_name='map_unresolved_resolved_location',
            name='unresolved_location_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.unresolved_location'),
        ),
        migrations.AddField(
            model_name='author',
            name='source_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.source'),
        ),
    ]
