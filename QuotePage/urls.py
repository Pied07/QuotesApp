
from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('create/',views.quote_create,name='quote_create'),
    path('register/',views.register,name='register'),
    path('delete/<int:quote_id>/',views.quote_delete,name='quote_delete'),
    path('edit/<int:quote_id>/',views.quote_edit,name='quote_edit'),
    path('search/',views.search,name='search'),
    path('delete_comment/<str:text>/',views.delete_comment,name='delete_comment'),
    path('download/<int:quote_id>/',views.download_quote_image,name='download_quote_image'),
]
