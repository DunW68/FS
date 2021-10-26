from datetime import datetime

from django.db import models

# Create your models here.


class Poll(models.Model):

    name = models.CharField(max_length=100, verbose_name='Poll`s name')
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Question(models.Model):

    choices = (('Text', 'Text'),
               ('One_choice', 'One_choice'),
               ('Many_choices', 'Many_choices'),
               )
    text = models.CharField(max_length=250, verbose_name='question')
    question_type = models.CharField(max_length=25, choices=choices)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class AnonData(models.Model):

    user = models.CharField(max_length=250)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=250)