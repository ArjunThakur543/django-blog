from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("addblog", views.addblog, name='addblog'),
    path("contact", views.contact, name='contact'),
    path("login",views.login,name='login'),
    path('blog/<str:slug>',views.blog,name='blog')
]

