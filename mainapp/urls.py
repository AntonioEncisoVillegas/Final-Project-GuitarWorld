from django.urls import path
from mainapp import views
urlpatterns = [
    path('home/', views.index, name="home"),
    path('', views.index),
    path('about-us/', views.aboutUs, name="about-us"),
    path('contact/', views.questionContact, name="question"),
    path('new/advice/', views.newAdvice, name="new-advice")
]          