from rest_framework import generics
from .models import Actor, Movie, Genre, Technician
from .serializers import MovieSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def add_movie(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from request body
            movie_data = json.loads(request.body)
            serializer = MovieSerializer(data=movie_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format in request body'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

def delete_actor(request):
    if request.method == 'POST':
        actor_id = request.POST.get('actor_id')  # Assuming actor_id is sent in the request body
        try:
            actor = Actor.objects.get(pk=actor_id)
            if actor.Movie.count() == 0:  # Check if actor is not associated with any movies
                actor.delete()
                return JsonResponse({'message': 'Actor deleted successfully'}, status=200)
            else:
                return JsonResponse({'error': 'Actor is associated with movies and cannot be deleted'}, status=400)
        except Actor.DoesNotExist:
            return JsonResponse({'error': 'Actor not found'}, status=404)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

class DirectorMoviesListAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        director_id = self.kwargs['director_id']
        return Movie.objects.filter(technicians__id=director_id)

class ActorMoviesListAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        actor_id = self.kwargs['actor_id']
        return Movie.objects.filter(actors__id=actor_id)

class MovieListCreateAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
