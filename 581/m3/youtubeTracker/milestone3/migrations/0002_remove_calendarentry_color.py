# Generated by Django 4.2.7 on 2023-11-05 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('milestone3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendarentry',
            name='color',
        ),
    ]