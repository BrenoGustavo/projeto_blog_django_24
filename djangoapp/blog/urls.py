from django.urls import path
from blog.views import index

#Colocando um namespace

app_name ='blog'

urlpatterns = [
    path('', index, name='index'),
]
