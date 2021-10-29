from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from animals.serializers import AnimalSerializer
from .models import Animal
from rest_framework import status


class AnimalView(APIView):
    def post(self, request):
        serialized = AnimalSerializer(data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    

    def get(self, request):
        animals = Animal.objects.all()
        serialized = AnimalSerializer(animals, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
