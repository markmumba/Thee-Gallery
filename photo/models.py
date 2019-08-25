from django.db import models

# Create your models here.
import datetime as dt


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title=models.CharField(max_length=60)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    post_date = models.DateTimeField(auto_now_add=True)
