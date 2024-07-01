from django.db import models # type: ignore
from django.contrib.auth.models import AbstractUser # type: ignore


class Country(models.Model):
    region = models.CharField(max_length = 20)
    country = models.CharField(max_length= 30)


    def __str__(self):
        return self.country
    


class Birds(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET("Unknown"))
    species = models.CharField(max_length= 20)
    descroption = models.CharField(max_length= 100)
    picture = models.CharField(max_length= 300)
    def __str__(self):
        return f"{self.species} _ {self.descroption} _ {self.picture} _ {self.country}"
    

class User(AbstractUser):
    birds = models.ManyToManyField(Birds, blank= True, related_name="birds")

