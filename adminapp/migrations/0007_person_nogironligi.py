# Generated by Django 4.1.3 on 2022-12-06 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_remove_ijtimoiyhimoya_slug_remove_tuman_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nogironligi',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
