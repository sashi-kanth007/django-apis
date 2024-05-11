from django.db import models

# Create your models here.
    
class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technician(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Actor(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    year_of_release = models.IntegerField()
    ratings = models.FloatField()
    genres = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)
    technician = models.ManyToManyField(Technician)
    
    def __str__(self):
        return self.name
