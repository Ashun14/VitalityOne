# Generated by Django 4.1.6 on 2023-04-10 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='healthcategory',
            old_name='heading',
            new_name='cat_title',
        ),
    ]
