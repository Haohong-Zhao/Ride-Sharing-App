from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),   # have to pass-in a name
    path('about', views.about, name='about')
]