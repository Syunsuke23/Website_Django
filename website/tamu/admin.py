from django.contrib import admin

from . models import Guest

class TampilanGuest(admin.ModelAdmin):
    list_display = ('nim', 'nama', 'kegiatan')
    list_display_links = (None)
    search_fields = ('nim', 'nama')

admin.site.register(Guest, TampilanGuest)
