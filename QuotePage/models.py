from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import os
from django.conf import settings

# Create your models here.
class Quote(models.Model):

    def get_font_family():
        font_dir = os.path.join(settings.BASE_DIR,"QuotesApp/static/fonts")
        font_files = os.listdir(font_dir)
        font_choice = []

        for font_file in font_files:
            if font_file.endswith(('.ttf')):
                font_name = os.path.splitext(font_file)[0].replace('_',' ').title()
                font_choice.append((font_file,font_name))


        return font_choice



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
    
    
