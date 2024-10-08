# Generated by Django 5.0.8 on 2024-09-27 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_notice_approved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=255)),
            ],
        ),
    ]
