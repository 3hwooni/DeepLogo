from django.shortcuts import render
from .models import Images
# from django.woon.models import model_to_dict
image_code = 4020180173210
queryset = Images.objects.get(application_num=image_code)
# image = model_to_dict(queryset)

def home(request) :
    return render(request,'woon/home.html')


def search(request) :
   
    return render(request,'woon/search.html',{"queryset":queryset})


def recommend(request) :
    return render(request,'woon/recommend.html')


def predict(request) :
    return render(request,'woon/predict.html')

def test(request) :
    return render(request,'woon/test.html',{"queryset":queryset})

