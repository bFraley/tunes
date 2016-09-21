from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ManyToManyField('Artist')
    tracks = models.ManyToManyField('Track') 
    genres = models.ManyToManyField('Genre')

    def __str__(self):
        return '{} by {}'.format(self.title, self.artist)


class Track(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ManyToManyField('Artist')
    genres = models.ManyToManyField('Genre')
    album_coll = models.ForeignKey('Album', null =True, blank=True)

    def __str__(self):
    	return '{} by {} from album: {}'.format(self.title, self.artist, self.album)


class Genre(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
