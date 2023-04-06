
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render

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

# logout
def login(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')
        user = authenticate(request, phone_number=phone_number, password=password)
        if user is not None:
            login(request, user)
            return redirect('account:homepage')
        else:
            error_message = 'Invalid username or password'
            return render(request, 'account/login.html', {'error_message': error_message})
    else:
        return render(request, 'account/login.html')

# def login(request):
#     if request.user.is_authenticated:
#         return redirect("account:index_page")

#     if request.method != "POST":
#         return render(request, "account/login.html")

#     phone_number = request.POST["phone_number"]
#     password = request.POST["password"]
#     if user := auth.authenticate(request, phone_number= phone_number, password=password):
#         auth.login(request, user)
#         messages.success(request, "You are now logged in")
#         return redirect("account:index_page")
#     messages.warning(request, "Invalid credentials")
#     return redirect("account:login")

def logout_user(request):
    logout(request)
    return redirect("account:register")

    


def HomePage(request):
    return render(request, "index.html")
  

