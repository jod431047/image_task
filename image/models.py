from django.db import models
from django.utils import timezone
# Create your models here.

COLOUR =(
    ('red','red'),
    ('blue','blue'),
    ('white','white'),
    ('black','black'),
    
)

class Image(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    colour = models.CharField(max_length=20,choices=COLOUR,default='red')
    create_date = models.DateTimeField(('create date'),default=timezone.now)
    
    
    def __str__(self):
        return self.name