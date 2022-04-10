from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Advert
from .forms import AdvertForm
from django.views.generic.edit import FormView


class AdvertList(generic.ListView):
    model = Advert
    queryset = Advert.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class AdvertInfo(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Advert.objects.filter(status=1)
        advert = get_object_or_404(queryset, slug=slug)

        return render(request, "advert_info.html", {
            "advert": advert,
        })


class PostAdvert(FormView):
    template_name = 'post_advert.html'
    form_class = AdvertForm
    success_url = 'home'
