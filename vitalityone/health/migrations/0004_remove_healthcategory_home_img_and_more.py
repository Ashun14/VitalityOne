# Generated by Django 4.1.6 on 2023-04-11 07:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_healthcategory_sub_cat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='healthcategory',
            name='home_img',
        ),
        migrations.RemoveField(
            model_name='healthpost',
            name='topics',
        ),
        migrations.AddField(
            model_name='healthpost',
            name='tags',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='healthpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='health.healthcategory'),
        ),
        migrations.AlterField(
            model_name='healthpost',
            name='input_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
