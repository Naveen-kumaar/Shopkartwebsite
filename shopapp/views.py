from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'shoptemp/index.html')

def Register(request):
    return render(request,'shoptemp/register.html')