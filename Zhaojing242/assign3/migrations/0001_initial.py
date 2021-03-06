# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-17 04:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_username', models.CharField(max_length=200)),
                ('comment_content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_size', models.IntegerField(default=0)),
                ('file_type', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=200)),
                ('project_date', models.CharField(max_length=200)),
                ('project_version', models.IntegerField(default=0)),
                ('project_summary', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_revision', models.IntegerField(default=0)),
                ('version_author', models.CharField(max_length=200)),
                ('version_msg', models.CharField(max_length=200)),
                ('version_date', models.CharField(max_length=200)),
                ('version_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign3.File')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign3.Project'),
        ),
        migrations.AddField(
            model_name='comment',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assign3.Project'),
        ),
    ]
