# Generated by Django 4.1.3 on 2022-12-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IjtimoiyHimoya',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=200)),
                ('familiya', models.CharField(max_length=200)),
                ('otasining_ismi', models.CharField(max_length=200)),
                ('passport_seriya', models.CharField(max_length=200)),
                ('kimga_murojaat_qilgan', models.CharField(max_length=200)),
                ('mablag_ajratgan_tashkilot', models.CharField(max_length=400)),
                ('summa', models.BigIntegerField()),
                ('photo', models.ImageField(blank=True, upload_to='images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('doimiy_yashash_manzili', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.tuman')),
                ('ijtimoiy_himoya', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.ijtimoiyhimoya')),
            ],
        ),
    ]
