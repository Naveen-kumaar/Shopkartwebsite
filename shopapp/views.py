from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'shoptemp/index.html')

def Register(request):
    return render(request,'shoptemp/register.html')


def Collections(request):
    category =Category.objects.filter(status=0)
    return render(request,'shoptemp/collections.html',{"category":category})

def CollectionView(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products = Product.objects.filter(category__name=name)
        return render(request,'Products/productsindex.html',{"products":products,"category":name})
    else:
        messages.warning(request,"NO Such Category Found")
        return redirect('collections')

    