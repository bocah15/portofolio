# Generated by Django 2.0.3 on 2018-03-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kehadiran', '0026_auto_20180301_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kehadiran',
            name='waktu_Mulai',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='kehadiran',
            name='waktu_Selesai',
            field=models.TimeField(),
        ),
    ]
