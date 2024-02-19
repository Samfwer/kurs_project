from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import AuthorViewSet,LabelViewSet,MusicViewSet,GenreViewSet,AlbumViewSet,MusicUploadView



router = DefaultRouter()

router.register(r'author',AuthorViewSet)
router.register(r'label',LabelViewSet)
router.register(r'music',MusicViewSet)
router.register(r'genre',GenreViewSet)
router.register(r'album',AlbumViewSet)
# router.register(r'music_pload',MusicUploadView)



urlpatterns = [
    path('', include(router.urls)),
    path('upload/', MusicUploadView.as_view(), name='music-upload'),

]