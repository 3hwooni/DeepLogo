from django.urls import path ,re_path

from . import views

urlpatterns = [
    path('', views.home ,name= 'home'),
    path('search/', views.search ,name= 'search'),
    path('recommend/', views.recommend ,name= 'recommend'),
    path('predict/', views.predict ,name= 'predict'),
    path('test/', views.test ,name= 'test'),

]