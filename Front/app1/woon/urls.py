from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('', views.home ,name= 'home'),
    path('search/', views.search ,name= 'search'),
    path('recommend/', views.recommend ,name= 'recommend'),
    path('predict/', views.predict ,name= 'predict'),
    path('test/', views.test ,name= 'test'),
    path('upload/', views.upload ,name= 'upload'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photos/upload/', views.upload_photo, name='upload_photo'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)