from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie_app.serializers import DirectorSerializer, MovieSerializer, ReviewSerializer
from movie_app.models import Director, Movie, Review


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_item_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not exist found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_item_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not exist found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_view(request):
    movies = Review.objects.all()
    serializer = ReviewSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_item_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not exist found'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_reviews_view(request):
    movie_reviews = Movie.objects.all()
    data = MovieSerializer(movie_reviews, many=True).data
    return Response(data=data)
