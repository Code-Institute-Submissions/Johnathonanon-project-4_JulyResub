from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Advert(models.Model):
    title = models.CharField(max_length=100, unique=False)
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    firearm_make = models.CharField(max_length=100, unique=False)
    firearm_model = models.CharField(max_length=100, unique=False)
    calibre = models.CharField(max_length=100, unique=False)
    price = models.IntegerField()
    description = models.TextField()
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
