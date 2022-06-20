from django.db import models

# Create your models here.

class Characteristic(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __repr__(self):
        return f"Characteristica {self.id} - {self.name}"
    