from django.shortcuts import render
from .forms import KvarteraForm
from django.shortcuts import redirect
from .models import Kvartera
def KvarteraView(request):
    if request.method == 'GET':
        form = KvarteraForm()
        return render(request, 'post/form.html', {'form': form})


        
    if request.method == 'POST':
        form = KvarteraForm(request.POST)
        if form.is_valid():
            # new_form = form.save(commit=False)
            price = request.POST['price']
            title = request.POST['title']
            b = Kvartera.objects.create(price=price, title=title)
            # price = form.cleaned_data.get('price')
            # title = form.cleaned_data.get('title')
            # new_form.price = price
            # new_form.title = title
            b.save()
            return redirect('account:hompage')
        else:
            return render(request, 'post/form.html', {'form': form})

def saveform(request):
    if request.POST:
        model = Kvartera()
        model.title = request.POST['title']
        model.price = request.POST['price']
        model.total_area = request.POST['total_area']
        model.description = request.POST['description']
        model.living_space = request.POST['living_space']
        model.number_rooms = request.POST['number_rooms']
        model.kitchen_area = request.POST['kitchen_area']
        model.floor = request.POST['floor']
        model.house_floor_plan = request.POST['house_floor_plan']
        # model.year_of_construction = request.POST['year_of_construction']
        print(request.POST.get('title'))
        
    
        model.save()    
        return redirect('account:homepage')
    return redirect("post:kvarteraview")
                