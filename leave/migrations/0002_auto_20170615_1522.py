# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-15 15:22
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='employee',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
