# Generated by Django 4.1.6 on 2023-04-10 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0013_workoutspost_author_alter_workoutspost_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutspost',
            name='sub_description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
