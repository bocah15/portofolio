# Generated by Django 2.0.3 on 2018-03-11 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0007_auto_20180308_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='alamat',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='jenis_kelamin',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='no_telepon',
        ),
    ]
