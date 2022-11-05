from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from musicapp.models import Artiste, Song, Lyrics


# Create your views here.
def Artiste_list_api(request):
    if request.method =="GET":
        Artistes = Artiste.object.all()
        serializer = ArtisteSerializer(Artistes, many=True)

        return JsonResponse(serializer.data, safe=False ) 
    
    
def Song_list_api(request):
    if request.method =="GET":
        Songs = Song.object.all()
        serializer = SongSerializer(Songs, many=True)

        return JsonResponse(serializer.data, safe=False ) 

def Lyric_list_api(request):
    if request.method =="GET":
        Lyrics = Lyric.object.all()
        serializer = LyricSerializer(Lyric_list_api, many=True)

        return JsonResponse(serializer.data, safe=False ) 









