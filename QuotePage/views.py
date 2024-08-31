from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import QuoteForm,UserForm,CommentForm
from .models import Quote,Like,Comment
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from PIL import ImageDraw,Image,ImageFont
import textwrap
from django.dispatch import receiver
import os
from django.db.models.signals import post_delete
from io import BytesIO
import requests
import cloudinary.uploader

# Create your views here.
def index(request):
    quotes = Quote.objects.all().order_by('-created_at')

    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        quote = Quote.objects.get(id=quote_id)
        if 'like' in request.POST:
            existing_like = Like.objects.filter(user=request.user,quote=quote)
            if not existing_like.exists():
                Like.objects.create(user=request.user,quote=quote)
            else:
                Like.objects.filter(user=request.user,quote=quote).delete()
        
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.quote = quote
            obj.save()

        return redirect('index')
    else:
        form = CommentForm()
        
    return render(request,'index.html',{'quotes':quotes,'form':form})
def delete_comment(request,text):
    quote_id = request.POST.get('quote_id')
    quote = Quote.objects.get(id=quote_id)
    if request.method == 'POST':
        Comment.objects.filter(user=request.user,quote=quote,text=text).delete()
        return redirect('index')
    return render(request,'index')

def add_text_to_image(image,text,author,fontcolor,fontsize, fontfamily):
    draw = ImageDraw.Draw(image)

    family = fontfamily

    font = ImageFont.load_default()

    maxwidth = image.width - 40

    wrapped_lines = textwrap.wrap(text,width=maxwidth//fontsize)
    
    total_height = sum(draw.textbbox((0,0),line,font=font)[3] for line in wrapped_lines)

    y =(image.height - total_height)/2

    for line in wrapped_lines:
        textbox = draw.textbbox((0,0),line,font=font)
        text_height = textbox[3] - textbox[1]
        text_width = textbox[2] - textbox[0]
        x = (image.width - text_width) / 2
        draw.text((x,y),line,font=font,fill=fontcolor)
        y += text_height

    copyright = "~ @"+author
    textbox = draw.textbbox((0,0),copyright,font=font)
    draw.text((image.width - (textbox[2]-textbox[0])-10,image.height - (textbox[3] - textbox[1]) - 10), copyright, font= font, fill=fontcolor)
    return image

@login_required
def quote_create(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST,request.FILES)
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            response = requests.get(quote.photo.url)
            image_path = Image.open(BytesIO(response.content))
            image_path = add_text_to_image(image_path,quote.quote_body,quote.name,quote.fontcolor,quote.fontsize,quote.fontfamily)
            image_byte_arr = BytesIO()
            image_path.save(image_byte_arr,format='JPEG')
            image_byte_arr.seek(0)

            upload_result = cloudinary.uploader.upload(image_byte_arr,public_id=quote.photo.public_id,overwrite=True)
            quote.photo = upload_result['url']
            quote.save()
            return redirect('index')
    else:
        form = QuoteForm()
    return render(request,'quote_form.html',{'form':form})

@login_required
def quote_edit(request,quote_id):
    quote = get_object_or_404(Quote,pk=quote_id, user=request.user)
    if request.method == 'POST':
        public_id = quote.photo.url.split('/')[-1].split('.')[0]
        cloudinary.uploader.destroy(public_id)
        form = QuoteForm(request.POST,request.FILES,instance=quote, initial={'photo':None})
        if form.is_valid():
            quote = form.save(commit=False)
            quote.user = request.user
            quote.save()
            response = requests.get(quote.photo.url)
            image_path = Image.open(BytesIO(response.content))
            image_path = add_text_to_image(image_path,quote.quote_body,quote.name,quote.fontcolor,quote.fontsize,quote.fontfamily)
            image_byte_arr = BytesIO()
            image_path.save(image_byte_arr,format='JPEG')
            image_byte_arr.seek(0)

            upload_result = cloudinary.uploader.upload(image_byte_arr,public_id=quote.photo.public_id,overwrite=True)
            quote.photo = upload_result['url']
            quote.save()
            return redirect('index')
    else:
        form = QuoteForm(instance=quote)
    return render(request,'quote_form.html',{'form':form})

@login_required
def quote_delete(request,quote_id):
    quote = get_object_or_404(Quote,pk=quote_id,user=request.user)
    if request.method == 'POST':
        public_id = quote.photo.url.split('/')[-1].split('.')[0]
        cloudinary.uploader.destroy(public_id)
        quote.delete()
        return redirect('index')
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request,'registration/register.html',{'form':form})

def search(request):
    query = request.GET['query']
    quotes = Quote.objects.filter(title__icontains=query).order_by('-updates_at') or Quote.objects.filter(quote_body__icontains=query).order_by('-updates_at') or Quote.objects.filter(name__icontains=query).order_by('-updates_at')

    if request.method == 'POST':
        quote_id = request.POST.get('quote_id')
        quote = Quote.objects.get(id=quote_id)
        if 'like' in request.POST:
            existing_like = Like.objects.filter(user=request.user,quote=quote)
            if not existing_like.exists():
                Like.objects.create(user=request.user,quote=quote)
            else:
                Like.objects.filter(user=request.user,quote=quote).delete()
        
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.quote = quote
            obj.save()

        return redirect('index')
    else:
        form = CommentForm()
    return render(request,'search.html',{'quotes':quotes, 'form':form})

def download_quote_image(request,quote_id):
    quote = get_object_or_404(Quote,id=quote_id)
    url = quote.photo.url

    response = requests.get(url)
    image_data = response.content

    response = HttpResponse(image_data,content_type='image/jpeg')
    response['Content-Disposition'] = f'attachment; filename="{quote.title}.JPG"'
    return response
