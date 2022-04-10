from django import forms
from .models import Advert


class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'type', 'featured_image', 'item_make', 'item_model', 'condition', 'calibre', 'price', 'description']
