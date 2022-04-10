from django.urls import path
from . import views


urlpatterns = [
    path('', views.AdvertList.as_view(), name='home'),
    path('post_advert/', views.PostAdvert.as_view(), name='post_advert'),
    path('<slug:slug>/', views.AdvertInfo.as_view(), name='advert_info'),
]