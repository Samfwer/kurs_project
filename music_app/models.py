from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 200 )
    psedonym = models.CharField(max_length = 200, blank=True, null=True)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    name_genre = models.CharField(max_length = 200 )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name_genre

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

class Album(models.Model):
    name = name = models.CharField(max_length = 200 )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Music(models.Model):
    name = models.CharField(max_length = 200)
    author = models.ForeignKey(Author,on_delete = models.CASCADE , related_name = 'Автор')
    duration = models.FloatField()
    data_released = models.DateTimeField()
    genre = models.ForeignKey(Genre,on_delete = models.CASCADE , related_name = 'Жанр')
    description = models.TextField(blank=True, null=True)
    label = models.CharField(max_length = 200 )
    album = models.ForeignKey(Album,on_delete = models.CASCADE , related_name = 'Альбом')
    music_file = models.FileField(upload_to='music_files/',null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Музыка'
        verbose_name_plural = 'Музыка'
     

class Label(models.Model):
    name = models.ForeignKey(Music,on_delete = models.CASCADE , related_name = 'Лейбл')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Лейбл'
        verbose_name_plural = 'Лейблы'


