from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    path('login/', views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('about/', views.about, name='about'),
]