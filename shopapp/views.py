from django.shortcuts import render,redirect
from . models import *
from django.contrib import messages
from shopapp.form import CustomUserForm
from django.shortcuts import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
import json

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
        
def CartPage(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        return render(request,"shoptemp/cart.html",{'cart':cart})
    else:
        return redirect("/")         

def removeCart(request,cid):
    cartitem = Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cartpage")    
    

def AddFav(request):    
    if request.headers.get('X-Requested-Width')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_id=data['pid']
            print(request.user.id)
            product_status =Product.objects.get(id=product_id)
            if product_status:
                if Favourite.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Favourite'}, status=200)
                else:
                    Favourite.objects.create(user=request.user,product_id=product_id)
                    return JsonResponse({'status':'Product Added to Favourite'}, status=200)
        else:
         return JsonResponse({'status':'Login to Add Favourite'}, status=200)
    else:
     return JsonResponse({'satuts':'Invalid Access'},status =200)


def AddtoCart(request):
    if request.headers.get('X-Requested-Width')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data = json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            print(request.user.id)
            product_status =Product.objects.get(id=product_id)
            
            if product_status:
                if Cart.objects.filter(user=request.user,product_id=product_id):
                    return JsonResponse({'status':'Product Already in Cart'},status=200)
                else:
                    if product_status.quantity >= product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'},status=200)
                    else:
                        return JsonResponse({'status':'Product Stock Not available'},status=200)
        else:
         return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
     return JsonResponse({'satuts':'Invalid Access'},status =200)
    
   
def FavViewPage(request):
    if request.user.is_authenticated:
        fav = Favourite.objects.filter(user=request.user)
        return render(request,"shoptemp/favviewpage.html",{'fav':fav})
    else:
        return redirect("/")   
    
def RemoveFavPage(request,fid):
    favitem = Favourite.objects.get(id=fid)
    favitem.delete()
    return redirect("/favviewpage")