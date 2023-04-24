# Generated by Django 4.1.6 on 2023-04-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0010_alter_workout_url_alter_workoutcategory_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='workouts_type',
            field=models.CharField(choices=[('tb', 'Total Body'), ('ub', 'Upper Body'), ('lb', 'Lower Body'), ('cr', 'Core')], default='tb', max_length=5),
        ),
    ]