# Generated by Django 3.0.2 on 2020-01-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_scraper', '0003_auto_20200128_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headline',
            name='headline',
            field=models.CharField(max_length=500),
        ),
    ]
