# Generated by Django 4.1.6 on 2023-04-10 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0016_rename_workoutspost_workoutposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutposts',
            name='reading_time',
            field=models.IntegerField(default=10),
        ),
    ]
