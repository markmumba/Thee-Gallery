from django.db import models


import datetime as dt

# Create your models here.
class categories(models.Model):
    categories =models.CharField(max_length=30)

    def __str__(self):
        return self.categories

    def save_categories(self):
        self.save()
    
class Location(models.Model):
    location =models.CharField(max_length=20)

    def __str__(self):
        return self.location

    class Meta:
        ordering = ['location']

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()

class Image(models.Model):

    image = models.ImageField(upload_to='images/')
    title=models.CharField(max_length=90)
    categories = models.ManyToManyField(categories)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()


    @classmethod
    def all_images(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(categories__category=search_term) 

        return images