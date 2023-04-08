from django.shortcuts import render

from django.shortcuts import redirect
from ..models import Kvartera,Category

def post_list_view(request, category_slug=None):
        posts = Kvartera.objects.filter(is_available=True)
        if category_slug:  
            category = Category.objects.get(slug=category_slug)
            posts = Kvartera.objects.filter(category=category, is_available=True)


        return render(request, "post/post.html", {"posts": posts,})
  


def post_detail_view(request, category_slug, product_slug):
    
    product = Kvartera.objects.get(category__slug=category_slug, slug=product_slug)
    product_images = Kvartera.images.all()
    context = {
        "product": product,
        "product_images": product_images,
    }
    return render(request, "post/post_detail.html", context)

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
 