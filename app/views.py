from django.shortcuts import render
from app.models import Profile

# Create your views here.
def home(request):
    return render(request,'main/home.html')


def signup(request):
    return render(request,'auth/signup.html')

def login(request):
    return render(request,'auth/login.html')

def user(request):
    return render(request,'auth/user.html')

def create(request):
    if request == "post":
            pass
    return render(request,'main/create.html')

def update(request):
    return render(request,'main/update.html')
