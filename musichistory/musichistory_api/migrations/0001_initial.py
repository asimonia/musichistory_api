# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-03 16:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('release_date', models.DateField()),
                ('album_length', models.TimeField()),
                ('num_stars', models.IntegerField()),
                ('label', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name_plural': 'Albums',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('year_established', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Artists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(choices=[('', ''), ('Pop', 'Pop'), ('Rock', 'Rock'), ('Metal', 'Metal'), ('Jazz', 'Jazz'), ('Country', 'Country'), ('Gospel', 'Gospel')], default='', max_length=20)),
                ('description', models.TextField(max_length=4000)),
            ],
            options={
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('song_length', models.TimeField()),
                ('release_date', models.DateField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musichistory_api.Album')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musichistory_api.Artist')),
                ('genres', models.ManyToManyField(to='musichistory_api.Genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musichistory_api.Artist'),
        ),
    ]
