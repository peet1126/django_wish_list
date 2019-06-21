from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import Wish

# Create your views here.
from django.http import HttpResponse


class index(ListView):
    model = Wish
    queryset = Wish.objects.all()

class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url = '/'

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'
    
    