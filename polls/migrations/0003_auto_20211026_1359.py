# Generated by Django 3.2.8 on 2021-10-26 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_alter_poll_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=250)),
                ('question_type', models.CharField(choices=[('Text', 'Text'), ('One_choice', 'One_choice'), ('Many_choices', 'Many_choices')], max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='poll',
            name='start_date',
            field=models.DateField(),
        ),
    ]