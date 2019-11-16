
from django.contrib import admin
from django.urls import path, include
from woon import views
urlpatterns = [
    path('', include('woon.urls')),
    path('admin/', admin.site.urls),
]
