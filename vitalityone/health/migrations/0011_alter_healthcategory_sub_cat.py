# Generated by Django 4.1.6 on 2023-04-15 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0010_alter_healthcategory_sub_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcategory',
            name='sub_cat',
            field=models.CharField(choices=[('ex', 'Explore'), ('hc', 'HealthCondition')], default='ex', max_length=2),
        ),
    ]
