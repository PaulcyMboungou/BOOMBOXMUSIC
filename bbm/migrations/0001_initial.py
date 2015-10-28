# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import bbm.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=100, verbose_name=b'Username', db_index=True)),
                ('email', models.EmailField(max_length=254, verbose_name=b'email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', bbm.models.MyUserManager()),
            ],
        ),
    ]
