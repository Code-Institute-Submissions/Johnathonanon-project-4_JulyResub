from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdvertList.as_view(), name='home'),
    path('my_adverts/', views.MyAdvertList.as_view(), name='my_adverts'),
    path('post_advert/', views.PostAdvert.as_view(), name='post_advert'),
    path('<slug:slug>/', views.AdvertInfo.as_view(), name='advert_info'),
]
