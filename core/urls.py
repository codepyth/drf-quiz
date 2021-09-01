from django.urls import path
from .views import *

urlpatterns = [
    path('', QuestionsView.as_view())
]
