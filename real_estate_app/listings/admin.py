from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor') # listing table in admin
  list_display_links = ('id', 'title') # turns these into links in table
  list_filter = ('realtor',)  # creates a filter which is by realtor
  list_editable = ('is_published',) # turns it to a checkbox to edit in table
  search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price') # creates search box
  list_per_page = 25

admin.site.register(Listing, ListingAdmin)
