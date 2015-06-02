# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('categories', models.CharField(max_length=255)),
                ('link_to_twitter', models.CharField(max_length=100)),
                ('amount_twitter_followers', models.CharField(max_length=15)),
                ('link_to_linkedin', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JournalistArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=255)),
                ('journalist', models.ForeignKey(to='medialist.Journalist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JournalistArticleMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('link', models.CharField(max_length=255)),
                ('journalist', models.ForeignKey(to='medialist.Journalist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JournalistComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('journalist', models.ForeignKey(to='medialist.Journalist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JournalistMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('categories', models.CharField(blank=True, max_length=255)),
                ('link_to_twitter', models.CharField(blank=True, max_length=100)),
                ('link_to_linkedin', models.CharField(blank=True, max_length=100)),
                ('activity', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='JournalistVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=100)),
                ('old_value', models.CharField(max_length=255)),
                ('new_value', models.CharField(max_length=255)),
                ('journalist', models.ForeignKey(to='medialist.Journalist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount_comments', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=255)),
                ('platforms', models.CharField(max_length=30)),
                ('categories', models.CharField(max_length=255)),
                ('alexa_rank', models.CharField(max_length=15)),
                ('link_to_alexa_rank', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=2)),
                ('amount_journalists', models.CharField(max_length=5)),
                ('email', models.CharField(max_length=100)),
                ('link_to_submit', models.CharField(max_length=255)),
                ('link_to_twitter', models.CharField(max_length=100)),
                ('amount_twitter_followers', models.CharField(max_length=15)),
                ('link_to_facebook', models.CharField(max_length=100)),
                ('amount_facebook_likes', models.CharField(max_length=15, verbose_name='Facebook')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaComment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('text', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(null=True, blank=True, to=settings.AUTH_USER_MODEL)),
                ('media', models.ForeignKey(to='medialist.Media')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=255)),
                ('platforms', models.CharField(blank=True, max_length=30)),
                ('categories', models.CharField(blank=True, max_length=255)),
                ('alexa_rank', models.CharField(blank=True, max_length=15)),
                ('language', models.CharField(blank=True, max_length=2)),
                ('amount_journalists', models.CharField(blank=True, max_length=5)),
                ('email', models.CharField(blank=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MediaVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('field', models.CharField(max_length=100)),
                ('old_value', models.CharField(max_length=255)),
                ('new_value', models.CharField(max_length=255)),
                ('media', models.ForeignKey(to='medialist.Media')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='journalistmeta',
            name='media',
            field=models.ForeignKey(to='medialist.Media'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='journalist',
            name='media',
            field=models.ForeignKey(to='medialist.Media'),
            preserve_default=True,
        ),
    ]
