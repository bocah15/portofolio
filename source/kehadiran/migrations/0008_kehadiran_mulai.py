# Generated by Django 2.0.2 on 2018-02-22 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0007_remove_kehadiran_mulai'),
    ]

    operations = [
        migrations.AddField(
            model_name='kehadiran',
            name='mulai',
            field=models.TimeField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
