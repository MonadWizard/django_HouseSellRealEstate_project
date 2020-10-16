from django.contrib import admin

from .models import Realtor

# change Register your models data's list views attribite.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp', 'hire_date')   # display items
    list_display_links = ('id', 'name', 'email')  #clickable display items
    list_filter = ('hire_date',)   # filter display items
    list_editable = ('is_mvp', )   # editable list item
    search_fields = ('name', 'phone', 'email')  # search panels filter items
    list_per_page = 3   # display list per page
admin.site.register(Realtor, RealtorAdmin)
