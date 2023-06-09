# Generated by Django 4.1.6 on 2023-04-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0005_alter_workout_url_alter_workoutcategory_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='url',
            field=models.CharField(default=models.CharField(max_length=50), max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='workoutcategory',
            name='url',
            field=models.CharField(default=models.CharField(default='', max_length=40), max_length=100, unique=True),
        ),
    ]
