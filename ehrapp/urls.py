from django.urls import path
from . import views

urlpatterns = [  
    path('',views.home,name='home'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),   
    path('register/', views.registerPage, name='register'), 
    path('doctor', views.doctor, name='doctor'), 
    path('individual', views.individual, name='individual') 
]