from django.shortcuts import render,redirect
from .models import Images
from .forms import PhotoForm
from .models import photo



image_code = 4020180173210
queryset = Images.objects.get(application_num=image_code)
from django.core.files.storage import FileSystemStorage
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

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url'] = fs.url(name)
        print(url)
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'woon/upload.html',context)
    

def photo_list(request):
    photos = photo.objects.all()
    return render(request, 'woon/photo_list.html',{'photos':photos})

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
        else:
            form = PhotoForm()
    form = PhotoForm()
    return render(request, 'woon/upload_photo.html',{'form':form})