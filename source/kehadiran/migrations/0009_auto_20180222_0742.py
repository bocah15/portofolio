# Generated by Django 2.0.2 on 2018-02-22 07:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0008_kehadiran_mulai'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kehadiran',
            name='mulai',
        ),
        migrations.AddField(
            model_name='kehadiran',
            name='selesai',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
