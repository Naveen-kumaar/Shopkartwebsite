from django.shortcuts import render
from . models import *

# Create your views here.
def home(request):
    return render(request,'shoptemp/index.html')

def Register(request):
    return render(request,'shoptemp/register.html')


def Collections(request):
    category =Category.objects.filter(status=0)
    return render(request,'shoptemp/collections.html',{"category":category})