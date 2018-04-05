# Generated by Django 2.0.2 on 2018-02-21 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Akun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis_akun', models.CharField(choices=[('dosen', 'Dosen'), ('admin', 'Administrator')], max_length=20)),
                ('akun', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nip', models.CharField(max_length=20)),
                ('alamat', models.TextField(blank=True)),
                ('jenis_kelamin', models.CharField(choices=[('pria', 'Laki-Laki'), ('wanita', 'Perempuan')], max_length=10)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('no_telepon', models.CharField(blank=True, max_length=30)),
                ('foto', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='akun',
            name='dosen',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dosen.Dosen'),
        ),
    ]