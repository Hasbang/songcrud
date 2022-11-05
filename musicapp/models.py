
from django.db import models
from datetime import datetime

# Create your models here.
class Artiste( models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class Song(models.Model):
    Artiste = models.ForeignKey(Artiste,on_delete = models.CASCADE)

    title = models.CharField(max_length=50)
    date_Released = models.DateTimeField(default= datetime.today)
    likes = models.CharField(max_length = 50)

    def __str__(self):
        return self.title


class Lyrics(models.Model):
    Song = models.ForeignKey(Song,on_delete =models.CASCADE)

    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content
