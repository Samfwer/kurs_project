from rest_framework import serializers
from .models import Author,Label,Music,Genre,Album
from django.shortcuts import render

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields  ='__all__'

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields  ='__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields  ='__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields  ='__all__'

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields  ='__all__'
        


