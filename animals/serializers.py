from rest_framework import serializers
from animals.models import Animal
from characteristcs.models import Characteristic
from characteristcs.serializers import CharacteristcSerializer
from group.models import Group
from group.serializers import GroupSerializer

class AnimalSerializer(serializers.Serializer):
        id              = serializers.IntegerField(read_only=True)
        name            = serializers.CharField(max_length=50)
        age             = serializers.FloatField()
        weight          = serializers.FloatField()
        sex             = serializers.CharField(max_length=15)
        characteristics = CharacteristcSerializer(many=True)
        group           = GroupSerializer()

        def create(self, validated_data:dict):
                group_data = validated_data.pop('group')
                characteristics_data = validated_data.pop('characteristics')

                group = Group.objects.get_or_create(group_data, **group_data)
                group = group[0]

                animal = Animal.objects.create(**validated_data, group=group)

                for char in characteristics_data:
                        characteristic = Characteristic.objects.get_or_create(char, **char)
                        characteristic = characteristic[0]
                        animal.characteristics.add(characteristic)


                return animal
        
        def update(self, instance:Animal, validated_data:dict):  

                non_editable_keys = ("group","sex",)

                characteristic_data = validated_data.pop("characteristics", None)

                if characteristic_data:
                        for char in  characteristic_data:
                                characteristic = Characteristic.objects.get_or_create(char, **char)
                                characteristic = characteristic[0]
                                print(characteristic.name)
                                setattr(instance.characteristics,'name', characteristic.name)
                                instance.characteristics.add(characteristic)


                for key, value in validated_data.items():
                        if key in non_editable_keys:
                                raise KeyError                        
                        setattr(instance, key, value)                

                instance.save()

                return instance

 