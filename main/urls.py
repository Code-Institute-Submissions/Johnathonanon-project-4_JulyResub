from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdvertList.as_view(), name='home'),
    path('<slug:slug>/', views.AdvertInfo.as_view(), name='advert_info'),
]