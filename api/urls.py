from django.urls import path

from .views import Artiste_list_api, Song_list_api,Lyric_list_api

urlpatterns =[
path("Artiste/", Artiste_list_api),
path("Song/", Song_list_api),
path("Artiste/", Lyric_list_api)

]