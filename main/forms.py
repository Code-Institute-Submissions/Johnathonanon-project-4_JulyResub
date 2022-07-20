"""
Main app forms file
"""
from django import forms
from .models import Advert


class AdvertForm(forms.ModelForm):
    """
    Uses Advert model to create form allowing user to post advert
    """
    class Meta:
        """
        Meta Class
        """
        model = Advert
        fields = (
            'title', 'type', 'featured_image',
            'item_make', 'item_model', 'condition',
            'calibre', 'price', 'description', 'contact_details'
        )

    def __init__(self, *args, **kwargs):
        """
        Custom init
        """
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['autofocus'] = True
