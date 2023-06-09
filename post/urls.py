# from .views import KvarteraView,saveform,post_list_view,post_detail_view
from .views.post import KvarteraView
from .views.post_list import saveform,post_detail_view,post_list_view
from django .urls import path
from .category_processors import all_categories,all_works
app_name = "post"  

urlpatterns = [
    path('list/',KvarteraView,name='kvarteraview'),
    path("saveform/", saveform, name="saveform"),
    path("list", post_list_view, name="post_list_view"),
    path("category/<slug:category_slug>/", post_list_view, name="post_list_view"),
    path('post-list/<slug:category>/<slug:subcategory>/', post_list_view, name='post_list_view'),
    path("<slug:category_slug>/<slug:product_slug>/", post_detail_view, name="post_detail_view"),
    path('categories/', all_categories, name='categories'),
    path('categories/', all_works, name='all_works'),
]