# Generated by Django 3.1.2 on 2020-11-09 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201109_0406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrowing',
            name='library',
        ),
    ]