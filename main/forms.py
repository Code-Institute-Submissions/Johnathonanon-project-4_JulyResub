from django import forms
from .models import Advert, Message


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'type', 'featured_image', 'item_make', 'item_model', 'condition', 'calibre', 'price', 'description', 'contact_details', 'seller']
