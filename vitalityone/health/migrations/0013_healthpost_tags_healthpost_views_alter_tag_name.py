# Generated by Django 4.1.6 on 2023-04-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0012_tag_remove_healthpost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthpost',
            name='tags',
            field=models.ManyToManyField(to='health.tag'),
        ),
        migrations.AddField(
            model_name='healthpost',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, choices=[('HNews', 'News'), ('HTips', 'Tips & Tricks')], max_length=10),
        ),
    ]
