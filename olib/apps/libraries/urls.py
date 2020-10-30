from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('libraries', views.LibraryViewSet)
router.register('books', views.BookViewSet, basename='book')
router.register('bookinfos', views.BookInfoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
