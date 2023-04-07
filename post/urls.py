from .views import KvarteraView,saveform
from django .urls import path
app_name = "post"  

urlpatterns = [
    path('',KvarteraView,name='kvarteraview'),
    path("saveform/", saveform, name="saveform"),
  
]