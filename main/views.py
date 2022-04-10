from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Advert
from .forms import AdvertForm
from django.views.generic.edit import CreateView


class AdvertList(generic.ListView):
    model = Advert
    queryset = Advert.objects.order_by('-created_on')
    template_name = 'index.html'


class AdvertInfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Advert.objects
        advert = get_object_or_404(queryset, slug=slug)

        return render(request, "advert_info.html", {
            "advert": advert,
        })


class PostAdvert(CreateView):
    model = Advert
    form_class = AdvertForm
    template_name = 'post_advert.html'
    success_url = 'home'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')


class MyAdvertList(generic.ListView):

    def get(self, request, *args, **kwargs):
        model = Advert
        queryset = Advert.objects.filter(seller_id=request.user.id).order_by('-created_on')

        return render(request, "my_adverts.html", {
            "advert": Advert,
        })