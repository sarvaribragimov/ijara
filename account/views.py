
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.contrib.auth.hashers import make_password
from .forms import RegistrForm
from django.contrib.auth import logout
from django.shortcuts import redirect


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
            return redirect('account:homepage')
        else:
            return render(request, 'account/register.html', {'form': form})

# logout

def logout_user(request):
    logout(request)
    return redirect("account:register")

    


def HomePage(request):
    return render(request, "index.html")
  

