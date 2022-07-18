
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Product

# Create your views here.
def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', context={'products': products})

class CatalogListView(generic.ListView):
    model = Product
    paginate_by = 3

class CatalogDetailView(generic.DetailView):
    model = Product


# Create base classes to CRUD data
#Create data
class ProductCreate(CreateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog')

#Update data
class ProductUpdate(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('catalog')

#Delete data
class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog')