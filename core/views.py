from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class QuestionsView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.is_valid())
            question = serializer.save()
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     question = Question.objects.all()
    #     serializer = QuestionSerializer(question)
    #     return Response(serializer.data)
