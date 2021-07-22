from django.urls import path

from . import views



urlpatterns = [

	path('sponser/', views.registerSponser, name="register"),

]