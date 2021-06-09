from django.contrib import admin
from .models import Project

admin.site.register(Project)    # needed to add in the admin to add portfolios into the db
