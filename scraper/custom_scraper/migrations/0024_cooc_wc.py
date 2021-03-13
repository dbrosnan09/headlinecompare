# Generated by Django 3.0.6 on 2020-10-21 18:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('custom_scraper', '0023_auto_20201021_1630'),
    ]

    operations = [
        migrations.CreateModel(
            name='cooc_wc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('newspaper', models.PositiveIntegerField()),
                ('base_word', models.CharField(max_length=500)),
                ('cooc', models.CharField(max_length=500)),
                ('coocc', models.PositiveIntegerField()),
            ],
        ),
    ]
