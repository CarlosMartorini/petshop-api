from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from animals.serializers import AnimalSerializer
from .models import Animal, Group, Characteristic
from rest_framework import status


class AnimalView(APIView):
    def post(self, request):
        data = request.data
        
        group = data.pop('group')

        if not Group.objects.filter(name=group['name']):
            new_group = Group.objects.create(**group)
        else:
            new_group = Group.objects.get(name=group['name'])

        new_animal = Animal.objects.create(**data, group=new_group)

        characteristics = data.pop('characteristics')

        for item in characteristics:
            item_name = item['name']

            if not Characteristic.objects.filter(name=item_name):
                new_item = Characteristic.objects.create(name=item_name)
            else:
                new_item = Characteristic.objects.get(name=item_name)
            
            new_animal.characteristics.add(new_item)

        new_animal.save()

        serialized = AnimalSerializer(new_animal).data

        return Response(serialized, status=status.HTTP_201_CREATED)
    

    def get(self, request):
        animals = Animal.objects.all()
        
        serialized = AnimalSerializer(animals, many=True)
        
        return Response(serialized.data, status=status.HTTP_200_OK)


class AnimalViewById(APIView):
    def get(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)

            serialized = AnimalSerializer(animal)

            return Response(serialized.data, status=status.HTTP_200_OK)
        
        except Animal.DoesNotExist:
            return Response({'error': 'Animal not found!'}, status=status.HTTP_404_NOT_FOUND)
    

    def delete(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)

            animal.delete()

            return Response('', status=status.HTTP_204_NO_CONTENT)
        
        except:
            return Response({'error': 'Animal not found!'}, status=status.HTTP_404_NOT_FOUND)
