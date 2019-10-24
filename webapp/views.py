from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from rest_framework import permissions
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *


def index(request):
    return HttpResponse("<H2>HEY! Welcome to MY_ECOM! </H2>")

def get_absolute_url():
    return settings.APP_URL

class CategoryList(ListView):
    model = Category

class CategoryDetail(DetailView):
    model = Category

class CategoryCreate(CreateView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = Category
    fields = ['name','description']
    success_url = 'categories'

class CategoryUpdate(UpdateView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = Category
    fields = ['name','description']
    success_url = get_absolute_url() + '/categories'

class CategoryDelete(DeleteView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    model = Category
    success_url = 'categories'

class ProductList(ListView):
    model = Product

class ProductDetail(DetailView):
    model = Product

class ProductCreate(CreateView):
    model = Product

class ProductUpdate(UpdateView):
    model = Product

class ProductDelete(DeleteView):
    model = Product

