from django.urls import path
from .views import ImageList,ImageDetail
from image.api import ImageListAPI 
from image.api import  ImageDetailAPI


app_name='Image'


urlpatterns = [

    
    path('todo/api/list',ImageListAPI.as_view()),
    path('todo/api/<int:pk>',ImageDetailAPI.as_view()),
    path('image/', ImageList.as_view()),
    path('image/<int:pk>', ImageDetail.as_view()),
    
    ]
