# Generated by Django 4.1.6 on 2023-04-12 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0027_remove_workoutpost_workouts'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutpost',
            name='workouts',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='fitness.workout'),
        ),
    ]