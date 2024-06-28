from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request,'main/home.html')

def about(request):
    return render(request,'main/about.html')

def contact(request):
    return render(request,'main/contact.html')

def create(request):
    return render(request,'main/create.html')

def update(request):
    return render(request,'main/update.html')

def user(request):
    return render(request,'main/user.html')
