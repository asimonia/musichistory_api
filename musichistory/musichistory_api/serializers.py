from django.contrib.auth.models import User
from rest_framework import serializers
from musichistory_api import models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password', 'groups',
                  'is_staff', 'is_active', 'is_superuser', 'last_login',
                  'date_joined',)


class GenreSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = models.Genre
		fields = ('label',)


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = models.Artist
		fields = ('name', 'year_established',)


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = models.Album
		fields = ('title', 'release_date', 'album_length', 'num_stars', 
			'label', 'artist', 'genres',)


class SongSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = models.Song
		fields = ('title', 'song_length', 'release_date', 'plays', 'artist',
			'album', 'user',)