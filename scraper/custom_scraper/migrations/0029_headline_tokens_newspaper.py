# Generated by Django 3.0.6 on 2020-11-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_scraper', '0028_headline_tokens'),
    ]

    operations = [
        migrations.AddField(
            model_name='headline_tokens',
            name='newspaper',
            field=models.PositiveIntegerField(default=5),
            preserve_default=False,
        ),
    ]
