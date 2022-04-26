from django.contrib import admin
from django.urls import path
from app import views
app_name = 'app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name="root"),
    path('home/', views.Home, name="Home"),
    path('login/', views.Login,name="Login"),
    path('register/', views.Registration,name="Register"),
    path('analyser/', views.analyser,name="main"),
    path('faq/', views.FAQ,name="faq"),
     path('About/', views.About,name="About"),
    path('signout/', views.signout,name="sins"),
]
