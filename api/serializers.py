from rest_framework import serializers

from musicapp.models import Artiste, Song, Lyrics


class ArtisteSerializer(serializers.ModelSerializer):
    class meta:
        model = Artiste

        fields = ["id", "first_name", "last_name", "age"]


class SongSerializer(serializers.ModelSerializer):
    class meta:
        model = Song
        
        fields = ["  Artiste", "title",  "date_Released" , "likes"]



        

class LyricSerializer(serializers.ModelSerializer):
    class meta:
        model = Lyrics
        
        fields = ["Song ", "content"]


