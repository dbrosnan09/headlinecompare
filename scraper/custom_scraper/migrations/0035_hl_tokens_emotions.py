# Generated by Django 3.0.6 on 2020-11-13 16:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('custom_scraper', '0034_hl_tokens'),
    ]

    operations = [
        migrations.CreateModel(
            name='hl_tokens_emotions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline_id', models.PositiveIntegerField()),
                ('newspaper', models.PositiveIntegerField()),
                ('word', models.CharField(max_length=500)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('link', models.CharField(max_length=1000)),
                ('day_order', models.PositiveIntegerField()),
                ('fear', models.PositiveIntegerField()),
                ('anger', models.PositiveIntegerField()),
                ('anticip', models.PositiveIntegerField()),
                ('trust', models.PositiveIntegerField()),
                ('surprise', models.PositiveIntegerField()),
                ('positive', models.PositiveIntegerField()),
                ('negative', models.PositiveIntegerField()),
                ('sadness', models.PositiveIntegerField()),
                ('disgust', models.PositiveIntegerField()),
                ('joy', models.PositiveIntegerField()),
            ],
        ),
    ]
