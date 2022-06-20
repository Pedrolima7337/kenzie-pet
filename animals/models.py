from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=50)
    age = models.FloatField()
    weight = models.FloatField()
    sex = models.CharField(max_length=15)

    group = models.ForeignKey('group.Group', on_delete=models.CASCADE, related_name='animais')

    characteristics = models.ManyToManyField('characteristcs.Characteristic', related_name='animais')

    def __repr__(self):
        return f"Animal {self.id} - {self.name}/{self.sex}"