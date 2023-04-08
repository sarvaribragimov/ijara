from django.shortcuts import render
from ..forms import KvarteraForm
from django.shortcuts import redirect
from ..models import Kvartera,Category
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

    
 