# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 07:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0007_remove_trascat_transact_with'),
    ]

    operations = [
        migrations.AddField(
            model_name='trascat',
            name='transact_with',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='technical.Student'),
        ),
    ]
