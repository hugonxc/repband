from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    name = models.CharField(unique=True, max_length=200)
    artist = models.CharField(unique=True, max_length=200)
    yt_link = models.CharField(unique=True, max_length=200)

class RepertoryMusic(models.Model):
    TONALITES = [
        ('C', 'C'),
        ('C#', 'C#'),
        ('Db', 'Db'),
        ('D', 'D'),
        ('D#', 'D#'),
        ('Eb', 'Eb'),
        ('E', 'E'),
        ('F', 'F'),
        ('F#', 'F#'),
        ('Gb', 'Gb'),
        ('G', 'G'),
        ('G#','G#'),
        ('Ab', 'Ab'),
        ('A', 'A'),
        ('A#', 'A#'),
        ('Bb', 'Bb'),
        ('B', 'B')
    ]
    tonality = models.CharField(
        max_length=3,
        choices=TONALITES,
        default='C',
    )

    music = models.ForeignKey(Music,on_delete=models.DO_NOTHING)
    rehearsed = models.BooleanField(default=False)
    note = models.CharField(unique=True, max_length=500)

class Repertory(models.Model):
    owner = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(unique=True, max_length=200)
    note = models.CharField(unique=True, max_length=500)    
    repertory_musics = models.ManyToManyField(RepertoryMusic)