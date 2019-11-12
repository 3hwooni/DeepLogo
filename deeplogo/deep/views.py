from django.shortcuts import render

# Create your views here.


def home(request) :
    return render(request,'deep/home.html')


def search(request) :
    return render(request,'deep/search.html')


def recommend(request) :
    return render(request,'deep/recommend.html')


def predict(request) :
    return render(request,'deep/predict.html')

