# Generated by Django 2.0.2 on 2018-02-22 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0009_auto_20180222_0742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kehadiran',
            name='selesai',
        ),
    ]
