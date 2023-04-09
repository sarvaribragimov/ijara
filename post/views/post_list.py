from django.shortcuts import render

from django.shortcuts import redirect
from ..models import Kvartera,Category
from ..forms import KvarteraForm
def post_list_view(request, category_slug=None):
        posts = Kvartera.objects.filter(is_available=True)
        if category_slug:  
            category = Category.objects.get(slug=category_slug)
            posts = Kvartera.objects.filter(category=category, is_available=True)


        return render(request, "post/post.html", {"posts": posts,})
  


def post_detail_view(request, category_slug, product_slug):
    
    post = Kvartera.objects.get(category__slug=category_slug, slug=product_slug)
    context = {
        "post": post,
    }
    return render(request, "post/post_detail.html", context)



def saveform(request):
    if request.method == 'POST':
        form = KvarteraForm(request.POST, request.FILES)
        if form.is_valid():
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            kvartera = Kvartera()
            kvartera.title = form.cleaned_data['title']
            kvartera.description = form.cleaned_data['description']
            kvartera.category = category
            kvartera.price = form.cleaned_data['price']
            kvartera.image = form.cleaned_data['image']
            kvartera.addrees = form.cleaned_data['addrees']
            kvartera.save()
            
    else:
        form = KvarteraForm()
    return render(request, 'post/form.html', {'form': form})


def saveform(request):
    if request.POST:
        category_id = str(request.POST.get('category'))
        category = Category.objects.get(id=category_id)
        model = Kvartera()
        model.category = category
        model.title = request.POST['title']
        model.price = request.POST['price']
        model.image = request.POST['image']
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
 