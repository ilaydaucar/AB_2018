# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-30 08:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='CityName')),
                ('code', models.CharField(max_length=3, verbose_name='CityCode')),
            ],
            options={
                'verbose_name': 'Şehir',
                'verbose_name_plural': 'Şehirler',
            },
        ),
        migrations.CreateModel(
            name='Town',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='TownName')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.City', verbose_name='Şehir')),
            ],
            options={
                'verbose_name': 'İlçe',
                'verbose_name_plural': 'İlçeler',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='town',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profile.Town', verbose_name='ilçe'),
        ),
    ]
