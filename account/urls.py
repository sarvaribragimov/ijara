from .views import register,HomePage,logout_user,login
from django .urls import path
app_name = "account"  

urlpatterns = [
    path('',HomePage,name='homepage'),
    path('register/',register,name='register'),
    path("logout/", logout_user, name="logout_user"),
    path('login/',login,name='login'),
]
