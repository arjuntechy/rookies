from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('pendulum/', views.pendulum, name='pendulum'),
    path('projectile/', views.projectile, name='projectile'),

]