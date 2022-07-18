"""
Imports
"""
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class UpdateAdvert(UpdateView):
    """
    Allows user to edit an advert
    """
    model = Advert
    form_class = AdvertForm
    template_name = 'edit_advert.html'
    success_url = reverse_lazy('my_adverts')


class DeleteAdvert(DeleteView):
    """
    Allows user to delete an advert
    """
    model = Advert
    form_class = AdvertForm
    template_name = 'delete_advert.html'
    success_url = reverse_lazy('home')


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
