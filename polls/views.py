from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import PollsSerializer, QuestionSerializer, AnonDataSerializer, ShowAnonDataSerializer, ShowResultsSerializer
from .models import Poll, Question, AnonData


class PollsView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PollsSerializer

    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollsSerializer(data=polls, many=True)
        serializer.is_valid()
        return Response(serializer.data)


class PollsChoice(APIView):
    serializer_class = AnonDataSerializer

    def get(self, request, pk):
        questions = Question.objects.filter(poll_id=pk)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        ip = request.META.get('REMOTE_ADDR')
        poll = pk
        question = request.data["question"]
        choice = request.data["choice"]
        data = {
            'user': f"{ip}",
            'poll': f"{poll}",
            'question': f"{question}",
            'choice': f"{choice}"
        }
        serializer = AnonDataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowResults(APIView):
    serializer_class = ShowAnonDataSerializer

    def get(self, request):
        ip = request.META.get('REMOTE_ADDR')
        data = AnonData.objects.filter(user=ip)
        serializer = ShowResultsSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        ip = request.data['user']
        print(ip)
        user = AnonData.objects.filter(user=ip)
        print(user)
        serializer = ShowResultsSerializer(user, many=True)
        return Response(serializer.data)
