from django.contrib import admin

# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

from .models import Meals , Category


class MealsAdmin( admin.ModelAdmin):  # instead of ModelAdmin
    list_display = ['name' ,'preperation_time', 'people', 'price']
    search_fields = ['name', 'description' ]
    list_filter = ('category','people')

admin.site.register(Meals , MealsAdmin)
admin.site.register(Category)