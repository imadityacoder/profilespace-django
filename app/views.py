from django.shortcuts import render,redirect
from app.models import Profile,Contact
from django.contrib.auth import login as auth_login, logout as auth_logout , authenticate 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        desc= request.POST.get('desc')

        form = Contact(name=name,email=email,desc=desc)
        form.save()
        messages.success(request, f'Your message is successfully submited!')
        
        return render(request,'main/home.html',{'form': form})

    return render(request,'main/home.html')
        



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.info(request,'Congratulation, You are now a profileSpace user!') 
            if user is not None:
                auth_login(request, user) 
                return redirect('create') 

    else:
        initial_data = {"username":'',"password1":'',"password2":''}
        form = UserCreationForm(initial = initial_data)
    return render(request, 'auth/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.info(request, f'Weclome, back {request.user.username}')
            return redirect('home')
        else:
            messages.warning(request, f"Please enter right password and username!")

    else:
        initial_data = {"username":'',"password":''}
        form = AuthenticationForm(initial = initial_data)
    return render(request, 'auth/login.html', {'form': form})

@login_required
def logout(request):
    auth_logout(request)
    messages.info(request,'Logout done!')
    return redirect('home')

@login_required
def user(request):
    return render(request,'auth/user.html')

@login_required
def create(request,username):     
    return render(request,'main/create.html')

@login_required
def update(request):
    return render(request,'main/update.html')
