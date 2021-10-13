from os import name
from django.contrib import admin
from django.urls import path
from Mainpage import views

urlpatterns = [
    path('', views.index, name='main'),
    path('button1/' ,views.button1,name='main1'),
    path('result1/', views.result, name='main2'),
    path('button2/', views.button2, name='main3'),
    path('result2/', views.diabetes, name='main4'),
    path('button3/', views.button3, name='main5'),
    path('result3/', views.salary, name='main6'),
    path('button4/', views.button4, name='main7'),
    path('result4/', views.forest, name='main8')
]
