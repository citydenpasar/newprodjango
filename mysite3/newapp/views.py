from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.


def movie_list(request):
    movies_object = Movies.objects.all()
    #pelajaran search
    movie_name = request.GET.get('movie_name')
    if movie_name !='' and movie_name is not None:
        # movies_object = Movies.objects.filter(name=movie_name) #filter biasa
        movies_object = Movies.objects.filter(name__icontains=movie_name)
    paginator = Paginator(movies_object, 2)
    page = request.GET.get('page')
    movies_object = paginator.get_page(page)
    context = {
        'movies_object': movies_object
    }
    return render(request, 'newapp/movies_list.html', context)
