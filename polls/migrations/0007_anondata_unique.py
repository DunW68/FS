# Generated by Django 3.2.8 on 2021-10-26 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20211026_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='anondata',
            name='unique',
            field=models.CharField(blank=True, default='1', max_length=10),
        ),
    ]
