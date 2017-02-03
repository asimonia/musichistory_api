from django.contrib import admin
from musichistory_api.models import Album, Artist, Genre, Song


admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Song)