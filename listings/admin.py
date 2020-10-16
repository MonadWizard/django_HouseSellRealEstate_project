from django.contrib import admin

from .models import Listing

# change Register your models data's list views attribite.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')   # display items
    list_display_links = ('id', 'title', 'realtor')  #clickable display items
    list_filter = ('realtor',)   # filter display items
    list_editable = ('is_published', 'price')   # editable list item
    search_fields = ('title', 'address', 'city', 'description', 'state', 'zipcode')  # search panels filter items
    list_per_page = 3   # display list per page

admin.site.register(Listing, ListingAdmin)
