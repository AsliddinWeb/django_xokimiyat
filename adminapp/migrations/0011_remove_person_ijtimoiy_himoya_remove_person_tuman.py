# Generated by Django 4.1.3 on 2022-12-07 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_alter_person_options_alter_person_ijtimoiy_himoya_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='ijtimoiy_himoya',
        ),
        migrations.RemoveField(
            model_name='person',
            name='tuman',
        ),
    ]
