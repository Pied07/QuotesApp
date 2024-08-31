from django.contrib import admin
from .models import Quote,Like,Comment

# Register your models here.
admin.site.register(Quote)
admin.site.register(Like)
admin.site.register(Comment)