# Generated by Django 4.1.6 on 2023-04-21 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('NNews', 'News'), ('NTips', 'Tips & Tricks')], max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='nutritionpost',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.RemoveField(
            model_name='nutritionpost',
            name='tags',
        ),
        migrations.AddField(
            model_name='nutritionpost',
            name='tags',
            field=models.ManyToManyField(to='nutrition.tag'),
        ),
    ]
