# Generated by Django 3.0.2 on 2020-03-27 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='artist',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='music',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='repertory',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='repertory',
            name='note',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='repertorymusic',
            name='note',
            field=models.CharField(max_length=500),
        ),
    ]