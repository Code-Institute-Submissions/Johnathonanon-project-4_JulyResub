"""
Imports
"""
from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class Advert(models.Model):

    """
    Main Advert Model user can create Advert instance from
    """

    TYPES = (
        ("firearm", "Firearm"),
        ("optic", "Optic"),
        ("accessory", "Accessory"),
    )

    CONDITIONS = (
        ("new", "New"),
        ("used", "Used"),
    )

    title = models.CharField(max_length=100, unique=False)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    type = models.CharField(max_length=20, choices=TYPES, default="Firearm")
    featured_image = models.ImageField(null=True, blank=True)
    item_make = models.CharField(max_length=100, unique=False)
    item_model = models.CharField(max_length=100, unique=False)
    condition = models.CharField(
        max_length=20, choices=CONDITIONS, default="New")
    calibre = models.CharField(
        max_length=100, unique=False, blank=True, default="N/A")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='seller')
    contact_details = models.CharField(
        max_length=100, unique=False, default="")
    created_on = models.DateField(auto_now_add=True)

    class Meta:

        """
        Meta Class
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)
