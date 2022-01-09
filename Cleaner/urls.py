from django.urls import path
from django.urls import path
from . import views

urlpatterns = [

    path('cleaner/', views.Cleaner, name='blog-about'),
]