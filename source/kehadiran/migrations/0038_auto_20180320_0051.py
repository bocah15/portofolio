# Generated by Django 2.0.3 on 2018-03-19 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0037_auto_20180320_0049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kehadiran',
            options={'ordering': ['dosen']},
        ),
    ]