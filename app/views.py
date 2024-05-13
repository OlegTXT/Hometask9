from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from app.models import Product


class Login(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('product_list')


class ProductList(PermissionRequiredMixin,ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    permission_required = ('app.view_product',)


class CreateProduct(PermissionRequiredMixin,CreateView):
    model = Product
    template_name = 'product_create.html'
    fields = ('__all__')
    success_url = reverse_lazy('product_list')
    permission_required = ('app.add_product',)


class UpdateProduct(PermissionRequiredMixin,UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = ('__all__')
    success_url = reverse_lazy('product_list')
    permission_required = ('app.change_product',)


@permission_required('app.delete_product')
def delete_product(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('product_list')