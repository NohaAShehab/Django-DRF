from django.urls import path
# from wishlist.api.views import movie_list,movie_details
from wishlist.api.views import MovieAPIView, MovieDetailAPIView,\
    StreamPlatformDetailAPIView, StreamPlatformAPIView, \
    WishListDetailAPIView,WishListAPIView
urlpatterns = [
    # path('list', movie_list, name="allmovies"),
    # path('<int:id>', movie_details, name="moviedetails"),
    path('list', MovieAPIView.as_view(), name="allmovies"),
    path("<int:id>", MovieDetailAPIView.as_view(), name="moviedetails"),
    path('wishlist', WishListAPIView.as_view(), name="all_lists"),
    path("wishlist/<int:id>", WishListDetailAPIView.as_view(), name="wishdetails"),
    path('streamlist', StreamPlatformAPIView.as_view(), name="stream"),
    path("streamlist/<int:id>", StreamPlatformDetailAPIView.as_view(), name="streamdetail"),

]
