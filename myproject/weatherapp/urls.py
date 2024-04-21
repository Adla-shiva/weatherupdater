
from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.index,name="index"),
    path('',views.login_page,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_page,name="logout"),
    path('user/',views.user_page,name="user"),
]
