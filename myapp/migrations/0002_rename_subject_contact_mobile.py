# Generated by Django 4.0.3 on 2022-03-09 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='subject',
            new_name='mobile',
        ),
    ]
