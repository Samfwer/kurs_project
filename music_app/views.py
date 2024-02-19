from django.shortcuts import render
from rest_framework import viewsets
from .models import Author,Label,Music,Genre,Album
from .serializers import AuthorSerializer,LabelSerializer,MusicSerializer,GenreSerializer,AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import MusicSerializer
# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]



class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]



class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name','author','duration','data_released','genre']


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name_genre',]


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]



class MusicUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        music_serializer = MusicSerializer(data=request.data)
        if music_serializer.is_valid():
            music_serializer.save()
            return Response(music_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(music_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
