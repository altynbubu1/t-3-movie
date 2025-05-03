from django.shortcuts import render
from main.models import Genre, Actor, Movie


def home(requests):
    genre = Genre.objects.all()
    actor = Actor.objects.all()
    movie = Movie.objects.all()
    context = {
        "genre":genre,
        "actor": actor,
        "movie": movie
    }
    return render(requests, "home.html", context)


def actors(requests):
    actor = Actor.objects.all()
    context = {
        "actor": actor,
    }
    return render(requests, "actors.html", context)