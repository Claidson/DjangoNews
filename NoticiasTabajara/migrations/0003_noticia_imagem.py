# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-01 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoticiasTabajara', '0002_auto_20171031_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='imagem',
            field=models.ImageField(default='static/images/django.jpg', upload_to='static/images/'),
        ),
    ]
