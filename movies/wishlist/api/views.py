from wishlist.models import Movie, WishList, StreamPlatform
from wishlist.api.serializer import MovieSeralizer,WishListSeralizer, StreamPlatformSeralizer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView



# @api_view()
# def movie_list(request):
#     movies = Movie.objects.all()
#     serilizer = MovieSeralizer(movies, many=True)
#     return Response(serilizer.data)

#
# @api_view(["GET", "POST"])
# def movie_list(request):
#     if request.method == "GET":
#         movies = Movie.objects.all()
#         serilizer = MovieSeralizer(movies, many=True)
#         return Response(serilizer.data)
#     elif request.method == "POST":
#         serializer = MovieSeralizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         # return Response(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # @api_view()
# # def movie_details(request, id):
# #     movie = get_object_or_404(Movie, pk=id)
# #     serilizer = MovieSeralizer(movie)
# #     return Response(serilizer.data)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def movie_details(request, id):
#     movie = get_object_or_404(Movie, pk=id)
#
#     if request.method == "GET":
#         serilizer = MovieSeralizer(movie)
#         return Response(serilizer.data)
#
#     if request.method == "PUT":
#         serializer = MovieSeralizer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#
#         # return Response(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     if request.method == "DELETE":
#         movie = get_object_or_404(Movie, pk=id)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# #Api view classes
class MovieAPIView(APIView):

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serilizer = MovieSeralizer(movies, many=True)
        return Response(serilizer.data)

    def post(self, request, format=None):
        serializer = MovieSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class MovieDetailAPIView(APIView):
    def get(self, request, id):
        movie = Movie.objects.get(pk=id)
        serilizer = MovieSeralizer(movie)
        return Response(serilizer.data)

    def put(self, request, id):
        movie = get_object_or_404(Movie, pk=id)
        serializer = MovieSeralizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request,id, format=None):
        movie = get_object_or_404(Movie,pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#########################################################33

class WishListAPIView(APIView):

    def get(self, request, format=None):
        movies = WishList.objects.all()
        serilizer = WishListSeralizer(movies, many=True)
        return Response(serilizer.data)

    def post(self, request, format=None):
        serializer = WishListSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class WishListDetailAPIView(APIView):
    def get(self, request, id):
        movie = WishList.objects.get(pk=id)
        serilizer = WishListSeralizer(movie)
        return Response(serilizer.data)

    def put(self, request, id):
        movie = get_object_or_404(WishList, pk=id)
        serializer = WishListSeralizer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request,id, format=None):
        movie = get_object_or_404(WishListSeralizer,pk=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


##################################################

class StreamPlatformAPIView(APIView):

    def get(self, request, format=None):
        platforms = StreamPlatform.objects.all()
        serilizer = StreamPlatformSeralizer(platforms, many=True)
        return Response(serilizer.data)

    def post(self, request, format=None):
        serializer = StreamPlatformSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class StreamPlatformDetailAPIView(APIView):
    def get(self, request, id):
        platform = StreamPlatform.objects.get(pk=id)
        serilizer = StreamPlatformSeralizer(platform)
        return Response(serilizer.data)

    def put(self, request, id):
        platform = get_object_or_404(StreamPlatform, pk=id)
        serializer = StreamPlatformSeralizer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request,id, format=None):
        platform = get_object_or_404(StreamPlatform,pk=id)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)







