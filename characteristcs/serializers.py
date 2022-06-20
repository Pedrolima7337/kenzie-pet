from rest_framework import serializers
from characteristcs.models import Characteristic

class CharacteristcSerializer(serializers.Serializer):
    id      = serializers.IntegerField(read_only=True)
    name    = serializers.CharField(max_length=20)

