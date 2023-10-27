from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Image


class ImageListAPI(generics.ListAPIView):
    queryset = Image.objects.all()
  
    
    
class ImageDetailAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
   