# Generated by Django 3.2.8 on 2021-10-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_anondata_unique'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anondata',
            name='unique',
        ),
    ]
