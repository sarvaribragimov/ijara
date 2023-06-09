from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from ..forms import KvarteraForm
from ..models import Category, Kvartera


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
        model.vositachilik_haqi = request.POST['vositachilik_haqi']
        # model.year_of_construction = request.POST['year_of_construction']
        model.save()    
        return redirect('account:homepage')
    return redirect("post:kvarteraview")
 