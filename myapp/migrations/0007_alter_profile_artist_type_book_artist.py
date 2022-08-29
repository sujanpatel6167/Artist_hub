# Generated by Django 4.0.3 on 2022-03-26 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_profile_artist_performance_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='artist_type',
            field=models.CharField(choices=[('singer', 'singer'), ('musician', 'musician'), ('painter', 'painter'), ('dancer', 'dancer')], max_length=100),
        ),
        migrations.CreateModel(
            name='Book_artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
                ('event_start_time', models.TimeField()),
                ('event_end_time', models.TimeField()),
                ('event_venue', models.TextField()),
                ('remarks', models.TextField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.profile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.user')),
            ],
        ),
    ]