
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from post.models import Kvartera,Category
from .forms import RegistrForm


def register(request):
    if request.method == 'GET':
        form = RegistrForm()
        return render(request, 'account/register.html', {'form': form})    
   
    if request.method == 'POST':
        form = RegistrForm(request.POST) 
        if form.is_valid():
            new_form = form.save(commit=False)
                    # data
            phone_number = form.cleaned_data.get("phone_number")
            first_name = form.cleaned_data.get("first_name")
            username = first_name  # get username from email
            password = form.cleaned_data.get("password")
            
            new_form.username = username
            new_form.phone_number = phone_number
            new_form.set_password(password)
            # new_form.password = password
            new_form.save()
    
            messages.success(request, 'You have singed up successfully.')
            # login(request, new_form)
            return redirect('account:login')
        else:
            return render(request, 'account/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect("account:homepage")

    if request.method != "POST":
        return render(request, "account/login.html")

    phone_number = request.POST["phone_number"]
    password = request.POST["password"]
    if user := auth.authenticate(request, phone_number= phone_number, password=password):
        auth.login(request, user)
        messages.success(request, "You are now logged in")
        return redirect("account:index_page")
    messages.warning(request, "Invalid credentials")
    return redirect("account:login")

def logout_user(request):
    logout(request)
    return redirect("account:register")

    


# def HomePage(request):
#     return render(request, "index.html")
  

def HomePage(request, category_slug=None):
    
    posts = Kvartera.objects.filter(is_available=True)
    if category_slug:  
        category = Category.objects.get(slug=category_slug)
        posts = Kvartera.objects.filter(category=category, is_available=True)

    return render(request, "index.html", {"posts": posts,})