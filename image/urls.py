from django.urls import path
from .views import ImageList,ImageDetail

app_name='Image'


urlpatterns = [

    
    
    path('image/', ImageList.as_view()),
    path('image/<int:pk>', ImageDetail.as_view()),
    
    ]
