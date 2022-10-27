from django.urls import path
from . import views


urlpatterns=[
    path('', views.shop, name='shop'),
    path('login', views.loginPage, name='login'),
    path('register', views.registrationPage, name='register'),
    path('logout/', views.logoutUser, name = 'logout'),
]