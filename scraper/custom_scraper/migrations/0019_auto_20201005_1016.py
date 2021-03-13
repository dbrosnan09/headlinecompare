# Generated by Django 3.0.6 on 2020-10-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_scraper', '0018_cooc_word_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word_count',
            old_name='newspaper',
            new_name='bbc',
        ),
        migrations.RenameField(
            model_name='word_count',
            old_name='word_count',
            new_name='fn',
        ),
        migrations.AddField(
            model_name='word_count',
            name='nyt',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word_count',
            name='overall',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
