from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # '' is the same as /
    path('about', views.about, name='about'),
]
