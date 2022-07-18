"""healcure URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from main import views
from catalog import views as c_views

urlpatterns = [
    #Main page
    path('', views.index, name='index'),
    # Product CRUD
    re_path(r'product/create/$', c_views.ProductCreate.as_view(), name='product_create'),
    re_path(r'product/update/(?P<pk>\d+)$', c_views.ProductUpdate.as_view(), name='product_update'),
    re_path(r'product/delete/(?P<pk>\d+)$',c_views.ProductDelete.as_view(), name='product_delete'),
    #Catalog page
    re_path(r'^catalog/$', c_views.CatalogListView.as_view(), name='catalog'),
    re_path(r'^catalog/(?P<pk>\d+)$', c_views.CatalogDetailView.as_view(), name='catalog-detail'),
    #Reserve page
    path('reserve', views.reserve_page, name='reserve'),
    #Accounts
    path('accounts/', include('django.contrib.auth.urls')),
    #Admin page
    path('admin', admin.site.urls),
]
