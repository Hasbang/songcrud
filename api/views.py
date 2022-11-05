from django.http import  HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from musicapp.models import Artiste, Song, Lyrics


# Create your views here.
@csrf_exempt
def Artiste_list_api(request):
    if request.method =="GET":
        Artistes = Artiste.object.all()
        serializer = ArtisteSerializer(Artistes, many=True)

        return JsonResponse(serializer.data, safe=False ) 
    if request.method == "Post":
        data = JSONParser().parse(request)
        serializer = ArtisteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
    return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def Song_list_api(request):

    if request.method =="GET":
        Songs = Song.object.all()
        serializer = SongSerializer(Songs, many=True)

        return JsonResponse(serializer.data, safe=False ) 
    
    if request.method == "Post":
        data = JSONParser().parse(request)
        serializer = SongSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
    return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def Lyric_list_api(request):
    if request.method =="GET":
        Lyrics = Lyric.object.all()
        serializer = LyricSerializer(Lyric_list_api, many=True)

        return JsonResponse(serializer.data, safe=False ) 
    
    if request.method == "Post":
        data = JSONParser().parse(request)
        serializer = LyricSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status= 201)
    return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def Artiste_details(request,pk):
    try:
        Artiste = Artiste.objects.get(pk=pk)
    except Artiste.DoesNotExist:
        return Httpresponse(staus=400)    


    if request.method == "GET":
        serializer= ArtisteSerializer(Artiste)    
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        data= JSONParser().parse(request) 
        serializer =ArtisteSerializer(Artiste, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        Artiste.delete()
        return HttpResponse(status=204)










