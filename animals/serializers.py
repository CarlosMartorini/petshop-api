from rest_framework import serializers
from characteristics.serializers import CharacteristicSerializer
from groups.serializers import GroupSerializer


class AnimalSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()

    group = GroupSerializer()
    characteristics = CharacteristicSerializer(many=True)