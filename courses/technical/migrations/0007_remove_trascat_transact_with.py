# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-22 07:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('technical', '0006_trascat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trascat',
            name='transact_with',
        ),
    ]
