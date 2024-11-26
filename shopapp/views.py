from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from django.shortcuts import HttpResponse

# Create your views here.
def home(request):
    products =Product.objects.filter(trending=1)
    return render(request,'shoptemp/index.html',{"products":products})

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

    
def ProductDetails(request,cname,pname):
    if(Category.objects.filter(name= cname,status=0)):
        if(Product.objects.filter(name= pname,status=0)):
            products = Product.objects.filter(name = pname,status=0).first()
            return render(request,"Products/ProductDetail.html",{"products":products})
        else:
            messages.error(request,"NO Such Product Found")
            return redirect('collections')
    else:
        messages.error(request,"NO Such Category Found")
        return redirect('collections')
        
            


