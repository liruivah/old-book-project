# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=20)),
                ('bookDetail', models.TextField(max_length=500)),
                ('bookImage', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sellerID', models.IntegerField()),
                ('course', models.CharField(max_length=20)),
                ('teacher', models.CharField(max_length=5)),
                ('pubDate', models.DateField(auto_now=True)),
                ('state', models.IntegerField()),
            ],
        ),
    ]
