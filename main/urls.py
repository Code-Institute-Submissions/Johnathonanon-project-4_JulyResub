from . import views
from django.urls import path


urlpatterns = [
    path('', views.AdvertList.as_view(), name='home')
]