# Generated by Django 4.1.6 on 2023-04-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0002_alter_workoutspost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutcategory',
            name='url',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
