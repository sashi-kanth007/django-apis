from rest_framework import serializers
from .models import Movie,Genre,Actor,Technician

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
        
class TechnicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Technician
        fields = '__all__'

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'