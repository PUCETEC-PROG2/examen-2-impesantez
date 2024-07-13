from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Movie

def index(request):
    movies = movies.objects.order_by('type')
    template = loader.get_template('index.html')
    return HttpResponse(template.render({'movie': movie}, request))

def movie(request, movie_id):
    movie = movie.objects.get(id=movie_id)
    template = loader.get_template('display_movie.html')
    context = {
        'movie': movie
    }
    return HttpResponse(template.render(context, request))