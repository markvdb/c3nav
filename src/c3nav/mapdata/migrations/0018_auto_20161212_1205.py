# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-12 12:05
from __future__ import unicode_literals

import c3nav.mapdata.fields
import c3nav.mapdata.models.interest
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mapdata', '0017_auto_20161208_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Name')),
                ('geometry', c3nav.mapdata.fields.GeometryField()),
                ('titles', c3nav.mapdata.fields.JSONField()),
            ],
            options={
                'default_related_name': 'areasofinterest',
                'verbose_name_plural': 'Areas of Interest',
                'verbose_name': 'Area of Interest',
            },
            bases=(models.Model, c3nav.mapdata.models.interest.MapItemOfInterestMixin),
        ),
        migrations.CreateModel(
            name='GroupOfInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(unique=True, verbose_name='Name')),
                ('titles', c3nav.mapdata.fields.JSONField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupsofinterest', to='mapdata.Package', verbose_name='map package')),
            ],
            options={
                'default_related_name': 'groupsofinterest',
                'verbose_name_plural': 'Groups of Interest',
                'verbose_name': 'Group of Interest',
            },
            bases=(models.Model, c3nav.mapdata.models.interest.MapItemOfInterestMixin),
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='areasofinterest', to='mapdata.GroupOfInterest', verbose_name='Groups of Interest'),
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areasofinterest', to='mapdata.Level', verbose_name='level'),
        ),
        migrations.AddField(
            model_name='areaofinterest',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='areasofinterest', to='mapdata.Package', verbose_name='map package'),
        ),
    ]