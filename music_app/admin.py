from django.contrib import admin
from .models import Author, Album, Music ,Label,Genre





# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display  = ('id','name','psedonym','biography',)
    list_display_links = ('id','name',)
    search_fields = ('id','name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display  = ('id','name','description',)
    list_display_links = ('id','name',)
    search_fields = ('id','name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display  = ('id','name_genre',)
    list_display_links = ('id','name_genre',)
    search_fields = ('id','name_genre',)

@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display  = ('id','name','description',)
    list_display_links = ('id','name',)
    search_fields = ('id','name',)


@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    list_display  = ('id','name','author','duration','data_released','genre','description','label','album',)
    list_display_links = ('id','name','author','duration','album',)
    search_fields = ('id','name','author',)

    
