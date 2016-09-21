from django.contrib import admin

# Register your models here.from django.contrib import admin

from .models import Album
from .models import Track
from .models import Genre
from .models import Artist

class AlbumAdmin(admin.ModelAdmin):
    fields = ('title', 'artist', 'tracks', 'genres')


class TrackAdmin(admin.ModelAdmin):
    fields = ('title', 'artist', 'genres', 'album_coll')

class GenreAdmin(admin.ModelAdmin):
    fields = ('name', 'category')

class ArtistAdmin(admin.ModelAdmin):
    fields = ('name')


admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Genre)
admin.site.register(Artist)
