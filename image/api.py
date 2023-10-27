from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import ImageSerializers
from .models import Image


class ImageListAPI(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers
  
    
    
class ImageDetailAPI(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializers