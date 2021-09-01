from rest_framework import serializers
from .models import *

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        field = 'choice_text'

class QuestionSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['question_text','question', 'choice_text']

    def create(self, validated_data):
        print(validated_data)
        choice_validated_data = validated_data.pop('question')
        print("prinnnnt", choice_validated_data)
        question = Question.objects.create(**validated_data)
        for each in choice_validated_data:
            choice = Choice.objects.create(choice_text=each)
            choice.save()
        return question