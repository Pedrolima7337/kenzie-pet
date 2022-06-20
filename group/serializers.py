from rest_framework import serializers

from group.models import Group

class GroupSerializer(serializers.Serializer):
    id              = serializers.IntegerField(read_only=True)
    name            = serializers.CharField(max_length=20)
    scientific_name = serializers.CharField(max_length=50)

