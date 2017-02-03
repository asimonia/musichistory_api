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
		model = Genre
		fields = ('label')


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Artist
		fields = ('name', 'year_established')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Album
		fields = ('title', 'release_date', 'album_length', 'num_stars', 
			'label', 'artist', 'genres')


class SongSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Song
		fields = ('title', 'song_length', 'release_date', 'plays', 'artist',
			'album', 'user')