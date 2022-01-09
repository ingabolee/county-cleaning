
from django.contrib import admin
from django.urls import path
from Cleaner.views import login_view, logout_view, register

urlpatterns = [
    path('', admin.site.urls),
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    
]
