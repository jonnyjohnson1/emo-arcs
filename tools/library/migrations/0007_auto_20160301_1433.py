# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20151214_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('gutenberg_id', models.IntegerField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='book',
            options={},
        ),
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.RemoveField(
            model_name='book',
            name='filename',
        ),
        migrations.AddField(
            model_name='book',
            name='downloads',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='epub_file_path',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='expanded_folder_path',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='from_gutenberg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='gutenberg_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='hash',
            field=models.CharField(default='aaa', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='lang_code_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='mobi_file_path',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pickle_object',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='txt_file_path',
            field=models.FilePathField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ignorewords',
            field=models.CharField(help_text='Comma separated list of words to ignore from this one.', max_length=400),
        ),
        migrations.AlterField(
            model_name='book',
            name='scaling_exponent',
            field=models.FloatField(help_text='Zipf law fit scaling exponent.'),
        ),
        migrations.AlterField(
            model_name='book',
            name='scaling_exponent_top100',
            field=models.FloatField(help_text='The scaling exponent fit across just the top 100.'),
        ),
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(to='library.Author'),
        ),
    ]
