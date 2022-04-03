from django import forms
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from autoslug import AutoSlugField

STATUS = ((0, "Draft"), (1, "Published"))


class Advert(models.Model):

    TYPES = (
        ("1", "Firearm"),
        ("2", "Optic"),
        ("3", "Accessory"),
    )

    title = models.CharField(max_length=100, unique=False)
    slug = AutoSlugField(populate_from='title')
    type = forms.ChoiceField(choices=TYPES)
    featured_image = models.ImageField()
    item_make = models.CharField(max_length=100, unique=False)
    item_model = models.CharField(max_length=100, unique=False)
    calibre = models.CharField(max_length=100, unique=False, blank=True, default="N/A")
    price = models.IntegerField()
    description = models.TextField()
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller_ad')
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Message(models.Model):
    advert = models.ForeignKey(
        Advert, on_delete=models.CASCADE, related_name='message')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Message {self.body} by {self.name}"

