from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),                     # /listings
    path('<int:listing_id>', views.listing, name='listing'),    # /listings/listing_id
    path('search', views.search, name='search'),                # /listings/search
]
