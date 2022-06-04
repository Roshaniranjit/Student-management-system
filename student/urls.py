from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create', views.createstudent, name='create'),
    path('update_stu/<str:pk>/', views.upDatestudent, name="update_stu"),
    path('delete_stu/<str:pk>/', views.DelStud, name="delete_stu"),

]
