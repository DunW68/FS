# Generated by Django 3.2.8 on 2021-10-26 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20211026_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onechoice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='onechoice',
            name='text',
        ),
        migrations.RemoveField(
            model_name='textchoice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='OneChoice',
        ),
        migrations.DeleteModel(
            name='TextChoice',
        ),
    ]