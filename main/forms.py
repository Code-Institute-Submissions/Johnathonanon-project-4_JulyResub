from django import forms
from .models import Message


class MessageForm(forms.Form):
    class Meta:
        model = Message
        fields = ('body',)
