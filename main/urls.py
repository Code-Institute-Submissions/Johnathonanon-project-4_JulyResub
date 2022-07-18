"""
Main URL config
"""
from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.AdvertList.as_view(), name='home'),
    path('my_adverts/', views.MyAdvertList.as_view(), name='my_adverts'),
    path('post_advert/',
         login_required(views.PostAdvert.as_view()), name='post_advert'),
    path('<slug>_edit_advert/',
         login_required(views.UpdateAdvert.as_view()), name='edit_advert'),
    path('<slug>/delete_advert',
         login_required(views.DeleteAdvert.as_view()), name='delete_advert'),
    path('<slug:slug>/', views.AdvertInfo.as_view(), name='advert_info'),
]
