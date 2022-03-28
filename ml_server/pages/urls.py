from django.urls import path

from .views import process, listModels

urlpatterns = [
    path('process', process, name='process'),
    path('list', listModels, name='listModels')
]
