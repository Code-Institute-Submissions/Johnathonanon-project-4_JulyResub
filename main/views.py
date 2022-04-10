"""
Imports
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic.edit import CreateView
from .models import Advert
from .forms import AdvertForm


class AdvertList(generic.ListView):
    """
    Generates list of advert objects to populate index.html
    """
    model = Advert
    queryset = Advert.objects.order_by('-created_on')
    template_name = 'index.html'


class AdvertInfo(View):
    """
    Allows user to view more information about a particular advert
    """
    def get(self, request, slug, *args, **kwargs):
        """
        Gets and renders selected advert
        """
        queryset = Advert.objects.all()
        advert = get_object_or_404(queryset, slug=slug)

        return render(request, "advert_info.html", {
            "advert": advert,
        })


class PostAdvert(CreateView):
    """
    Allows user to post an advert
    """
    model = Advert
    form_class = AdvertForm
    template_name = 'post_advert.html'
    success_url = 'home'

    def post(self, request, *args, **kwargs):
        print("processing form")
        form = self.form_class(request.POST)
        if form.is_valid():
            print("about to save form")
            form.save()
        return redirect('home')


class MyAdvertList(generic.ListView):
    """
    Generates list of users posted ads
    """
    def get(self, request, *args, **kwargs):
        queryset = Advert.objects.filter(
            seller__id=request.user.id).order_by('-created_on')

        return render(request, "my_adverts.html", {
            "advert_list": queryset,
        })
