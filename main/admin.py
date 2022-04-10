from django.contrib import admin
from .models import Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):

    list_filter = ('created_on',)
    list_display = ('title', 'seller', 'created_on')
    search_fields = ['title', 'description', 'firearm_make']
