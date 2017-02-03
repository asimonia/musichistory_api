from django.contrib.auth.models import User
from django.db import models


class Genre(models.Model):
	"""
	The genres table contains the various genres related to the songs.  Songs
	can fit into more than one genre, or none at all.
	"""
	label = models.CharField(max_length=20, unique=True)

	class Meta:
		verbose_name_plural = 'Genres'

	def __str__(self):
		return '{}'.format(self.label)


class Artist(models.Model):
	"""
	This table contains the name of the artist and the year the artist was established.
	"""
	name = models.CharField(max_length=40)
	year_established = models.IntegerField()

	class Meta:
		verbose_name_plural = 'Artists'

	def __str__(self):
		return '{}'.format(self.name)


class Album(models.Model):
	"""
	This table contains the albums and the related information.
	"""
	title = models.CharField(max_length=40)
	release_date = models.DateField('release date')
	album_length = models.DurationField('album length')
	num_stars = models.IntegerField()
	label = models.CharField(max_length=40)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	genres = models.ManyToManyField(Genre)

	class Meta:
		verbose_name_plural = 'Albums'

	def __str__(self):
		return '{}'.format(self.title)


class Song(models.Model):
	"""
	This table contains a list of songs and the related information.
	"""
	title = models.CharField(max_length=40)
	song_length = models.DurationField('track length')
	release_date = models.DateField('release date')
	plays = models.IntegerField(default=0)
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		verbose_name_plural = 'Songs'

	def __str__(self):
		return '{}'.format(self.title)
