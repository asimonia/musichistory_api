from django.contrib.auth.models import User
from musichistory_api import serializers, models
from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()


class GenreViewSet(viewsets.ModelViewSet):
	queryset = models.Genre.objects.all()
	serializer_class = serializers.GenreSerializer


class ArtistViewSet(viewsets.ModelViewSet):
	queryset = models.Artist.objects.all().order_by('-name')
	serializer_class = serializers.ArtistSerializer


class AlbumViewSet(viewsets.ModelViewSet):
	queryset = models.Album.objects.all().order_by('-artist')
	serializer_class = serializers.AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
	queryset = models.Song.objects.all().order_by('-album')
	serializer_class = serializers.SongSerializer