from django.urls import path, include

from ReadBook import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "ReadBook"

urlpatterns = [

path('', views.loadBook, name="premiumbook"),
path('addbook/', views.addBook, name="addbook"),
path('description/<int:bid>/', views.bookDescription, name='description'),
path('delete/<int:bid>/', views.deleteBook, name='deletebook'),
]

# so we can upload files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)