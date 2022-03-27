from django.urls import path

from .views import HomePageView, process

urlpatterns = [
    path('process', process, name='process')
]
