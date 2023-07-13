from django.shortcuts import render
from .forms import image
from .models import img
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = image(request.POST,request.FILES)
        if form.is_valid():
            form.save()        
    form = image()
    Images = img.objects.all()
    return render(request,'imageuploadapp/home.html',{'form':form,'Images':Images})