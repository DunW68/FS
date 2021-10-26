from .models import Poll, Question, AnonData
from rest_framework import serializers


class PollsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('name', 'description', 'end_date')


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnonDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonData
        fields = ('user', 'poll', 'question', 'choice')


class ShowAnonDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonData
        fields = ('user', )


class ShowResultsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnonData
        fields = ('poll', 'question', 'choice')