from django.shortcuts import render
from .models import Images
# Create your views here.
def home(request) :
    return render(request,'woon/home.html')


def search(request) :
   
    return render(request,'woon/search.html',)


def recommend(request) :
    return render(request,'woon/recommend.html')


def predict(request) :
    return render(request,'woon/predict.html')

