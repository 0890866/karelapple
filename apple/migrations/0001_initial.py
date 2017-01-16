# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-16 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apple_name', models.CharField(max_length=100)),
                ('ripening_date', models.CharField(blank=True, default='-', max_length=300)),
                ('eating', models.BooleanField()),
                ('cooking', models.BooleanField()),
                ('sauce', models.BooleanField()),
                ('pie', models.BooleanField()),
                ('juice', models.BooleanField()),
                ('butter', models.BooleanField()),
                ('notes', models.CharField(blank=True, default='-', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(db_index=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('steps', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('picture', models.FileField(upload_to='')),
                ('apple', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apple.AppleType')),
                ('ingredients', models.ManyToManyField(related_name='RecipesIngredients', to='apple.Ingredients')),
            ],
        ),
    ]