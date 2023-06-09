# Generated by Django 4.1.6 on 2023-04-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0011_alter_healthcategory_sub_cat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('HNews', 'Health News'), ('NNews', 'Nutrition News'), ('HFact', 'Health Tips'), ('NNews', 'Nutriton Tips')], max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='healthpost',
            name='tags',
        ),
    ]
