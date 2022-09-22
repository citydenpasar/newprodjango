from django.shortcuts import render
from .models import Movies
# Create your views here.


def movie_list(request):
    movies_object = Movies.objects.all()
    context = {
        'movies_object': movies_object
    }
    return render(request, 'newapp/movies_list.html', context)
