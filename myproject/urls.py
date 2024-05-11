"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
   path('admin/', admin.site.urls),
    path('movies/', views.MovieListCreateAPIView.as_view(),name='movie-list-create'),
    path('movies/<int:pk>/', views.MovieRetrieveUpdateAPIView.as_view(), name='movie-retrieve-update'),
    path('actors/<int:actor_id>/movies/', views.ActorMoviesListAPIView.as_view(), name='actor-movies-list'),
    path('directors/<int:director_id>/movies/', views.DirectorMoviesListAPIView.as_view(), name='director-movies-list'),
    path('addmovies/',views.add_movie,name='add-movie'),
    path('delete_actor/', views.delete_actor, name='delete-actor'),
]
