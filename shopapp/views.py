from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from shopapp.form import CustomUserForm
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    products =Product.objects.filter(trending=1)
    return render(request,'shoptemp/index.html',{"products":products})

def Register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success you can Login Now ...")
            return redirect('/login')
    return render(request,'shoptemp/register.html',{"form":form})

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:

        if request.method == 'POST':
            name = request.POST.get('username')
            pwd = request.POST.get('password')
            user = authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid user name or password")
                return redirect("login/")

        return render (request,'shoptemp/login.html')


def logoutPage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logout Successfully")
    return redirect("/")


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
        
            


def AddtoCart(request):
    pass