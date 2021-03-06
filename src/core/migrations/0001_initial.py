# Generated by Django 3.0.2 on 2020-01-29 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('artist', models.CharField(max_length=200, unique=True)),
                ('yt_link', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepertoryMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tonality', models.CharField(choices=[('C', 'C'), ('C#', 'C#'), ('Db', 'Db'), ('D', 'D'), ('D#', 'D#'), ('Eb', 'Eb'), ('E', 'E'), ('F', 'F'), ('F#', 'F#'), ('Gb', 'Gb'), ('G', 'G'), ('G#', 'G#'), ('Ab', 'Ab'), ('A', 'A'), ('A#', 'A#'), ('Bb', 'Bb'), ('B', 'B')], default='C', max_length=3)),
                ('rehearsed', models.BooleanField(default=False)),
                ('note', models.CharField(max_length=500, unique=True)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.Music')),
            ],
        ),
        migrations.CreateModel(
            name='Repertory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('note', models.CharField(max_length=500, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('repertory_musics', models.ManyToManyField(to='core.RepertoryMusic')),
            ],
        ),
    ]
