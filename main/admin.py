from django.contrib import admin
from .models import Advert, Message


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):

    list_filter = ('status', 'created_on')
    list_display = ('title', 'seller', 'status', 'created_on')
    search_fields = ['title', 'description', 'firearm_make']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'created_on')
    list_display = ('name', 'body', 'advert', 'created_on', 'approved')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_message']

    def approve_message(self, request, quesryset):
        quesryset.update(approved=True)
