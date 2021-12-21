from django.shortcuts import render
from wishlist.models import Movie
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.forms.models import model_to_dict
import json


# Create your views here.

def movie_list(request):
    movies = Movie.objects.all()
    data = list(movies.values())
    return JsonResponse(data, safe=False)


def movie_details(request, id):
    movie = get_object_or_404(Movie, pk=id)
    # data = serializers.serialize('json', [ movie, ])
    dict_obj = model_to_dict(movie)
    return JsonResponse(json.dumps(dict_obj), safe=False)
