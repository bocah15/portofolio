# Generated by Django 2.0.3 on 2018-03-17 10:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0009_auto_20180313_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='hallo',
            field=models.CharField(default=django.utils.timezone.now, max_length=5),
            preserve_default=False,
        ),
    ]