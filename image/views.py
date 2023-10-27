from django.shortcuts import render
from .models import Image
from django.views import generic



# Create your views here.

class ImageList(generic.ListView):
    model = Image
    
    
class ImageDetail(generic.DetailView):
    model = Image