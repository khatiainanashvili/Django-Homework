from django.db import models # type: ignore

# Create your models here.

class Birds(models.Model):
    species = models.CharField(max_length= 20)
    descroption = models.CharField(max_length= 100)
    picture = models.CharField(max_length= 300)
    def __str__(self):
        return f"{self.species} _ {self.descroption} _ {self.picture}"