from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import os
from django.conf import settings
import cloudinary.api

# Create your models here.
class Quote(models.Model):

    def get_font_family():
        response = cloudinary.api.resources(type="upload",resource_type="raw",max_results=100)

        font_choice = [(resource['public_id'], resource['secure_url']) for resource in response['resources'] if resource["public_id"].lower().endswith(".ttf")]
        formatted_choices = [(url, url.split('/')[-1].split('_')[0]) for _,url in font_choice]

        return formatted_choices



    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    quote_body = models.TextField(max_length=600)
    photo = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now=True)
    updates_at = models.DateTimeField(auto_now=True)
    caption = models.TextField(max_length=1000,null=True,blank=True)
    fontcolor = models.CharField(max_length=10,default='#000000')
    fontsize = models.IntegerField(default=20)
    fontfamily = models.CharField(max_length=100,choices=get_font_family(),default="arial.ttf")


    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE,related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} liked {self.quote.title}'
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.quote.title}'
    
    
