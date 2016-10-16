# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 11:13
from __future__ import unicode_literals

import c3nav.mapdata.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Name')),
                ('geometry', c3nav.mapdata.fields.GeometryField()),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doors', to='mapdata.Level', verbose_name='level')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doors', to='mapdata.Package', verbose_name='map package')),
            ],
            options={
                'verbose_name_plural': 'Doors',
                'verbose_name': 'Door',
                'default_related_name': 'doors',
            },
        ),
        migrations.CreateModel(
            name='Obstacle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Name')),
                ('geometry', c3nav.mapdata.fields.GeometryField()),
                ('height', models.DecimalField(decimal_places=2, max_digits=4, null=True, verbose_name='height of the obstacle')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obstacles', to='mapdata.Level', verbose_name='level')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='obstacles', to='mapdata.Package', verbose_name='map package')),
            ],
            options={
                'verbose_name_plural': 'Obstacles',
                'verbose_name': 'Obstacle',
                'default_related_name': 'obstacles',
            },
        ),
    ]