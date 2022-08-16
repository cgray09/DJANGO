from django.contrib import admin
from django.conf.urls import include, url
from parts_api import views

urlpatterns = [
    url("admin/", admin.site.urls),
    url("part/update/(?P<part_id>\d+)/$", views.update_part, name="update"),
    url("", views.home, name="home")
]
