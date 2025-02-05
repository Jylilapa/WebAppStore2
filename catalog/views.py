from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class HomeListView(ListView):
    model = Product


class ContactsTemplateView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductDetailView(DetailView):
    model = Product
