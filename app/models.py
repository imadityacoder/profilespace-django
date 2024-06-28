from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from autoslug import AutoSlugField


class Gender(models.Model):
    gender = models.CharField(max_length=50)
    def __str__(self):
        return self.gender

class Profile(models.Model):
    name = models.CharField(max_length=254)
    slug = AutoSlugField(populate_from='username',unique=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    age = models.PositiveIntegerField()
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    pic = models.ImageField(upload_to="images/")
    institution_name = models.CharField(max_length=254)
    degree = models.CharField(max_length=254)
    field = models.CharField(max_length=254)
    skills = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    email= models.EmailField(max_length=254)
    bio = models.TextField()
    created_at = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name + " - " + str(self.author) + " | " + str(self.email)
