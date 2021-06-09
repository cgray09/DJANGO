from django.urls import path
from . import views

app_name = 'blog' # to reference these paths in our templates/pages (may even reach further) - may have many other apps w/ the same routes so helps
                  # django out

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'), # route - blog/ (home in blog app)
    path('<int:blog_id>/', views.detail, name='detail'),
]
