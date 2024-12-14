from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def helpPage(request):
    return render(request,'help.html')

def supportPage(request):
    return render(request,'support.html')