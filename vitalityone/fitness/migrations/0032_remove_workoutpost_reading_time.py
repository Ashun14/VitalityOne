# Generated by Django 4.2 on 2023-04-25 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0031_alter_workoutpost_workouts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutpost',
            name='reading_time',
        ),
    ]