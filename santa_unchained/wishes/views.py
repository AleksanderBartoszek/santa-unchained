from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from .forms import WishListWithAddressAndItemsForm
from .models import WishList
from django.views.generic.edit import CreateView

class WishListSuccessView(TemplateView):
    template_name = "wishes/wishlist_success.html"

class WishListDetailView(DetailView):
    template_name = 'wishes/wishlist_detail.html'
    model = WishList


class WishListFormView(CreateView):
    model = WishList
    form_class = WishListWithAddressAndItemsForm
    #template_name = 'wishes/wishlist_form.html'

    def get_success_url(self):
        return reverse("wishes:success", kwargs={"slug": self.object.slug})
