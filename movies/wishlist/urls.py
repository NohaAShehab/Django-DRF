from django.urls import path
from wishlist.views import movie_list,movie_details
urlpatterns = [
    path('list', movie_list, name="allmovies"),
    path('<int:id>', movie_details, name="moviedetails"),
]