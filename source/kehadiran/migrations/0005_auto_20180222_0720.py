# Generated by Django 2.0.2 on 2018-02-22 07:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0004_auto_20180221_1614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kehadiran',
            name='mulai',
        ),
        migrations.AddField(
            model_name='kehadiran',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='kehadiran',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
