from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm, ProductModeratorForm
from catalog.models import Product, Category
from catalog.services import get_product_from_cache, ProductsListCategory


class HomeListView(ListView):
    model = Product

    def get_queryset(self):
        return get_product_from_cache()


class CategoryListView(ListView):
    model = Product
    template_name = "catalog/category_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = Category.object.name
        context["products"] = ProductsListCategory.get_products_category(category)
        return context



class ContactsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "catalog/contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalog/product_form.html"
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.can_unpublish_product"):
            return ProductModeratorForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm("product.delete_product"):
            return ProductModeratorForm
        raise PermissionDenied
