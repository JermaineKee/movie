# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Rater',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('occupation', models.CharField(max_length=40)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('zipcode', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('rating', models.IntegerField()),
                ('movie', models.ForeignKey(to='cinemaapp.Movie')),
                ('rater', models.ForeignKey(to='cinemaapp.Rater')),
            ],
        ),
    ]
