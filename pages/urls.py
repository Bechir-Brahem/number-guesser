from django.urls import path

from .views import HomePageView, process

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('process', process, name='process')
]
