from django.shortcuts import render 
from django.http import HttpResponse
from .forms import coordinateForm

# Create your views here.
def home(request):
    
    return render(request, 'motion/home.html')

def static(request):
    my_form = coordinateForm()
    context = {
        "form":my_form
    }
    return render(request,'motion/static.html', context)