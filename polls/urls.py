from django.urls import path, include
from django.contrib import admin
from .views import PollsView, PollsChoice, ShowResults

urlpatterns = [
    path('polls/', PollsView.as_view()),
    path('polls/<int:pk>/', PollsChoice.as_view()),
    path('polls/show_results', ShowResults.as_view())
]