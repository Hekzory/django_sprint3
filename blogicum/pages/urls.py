from django.urls import path
from . import views

app_name = 'pages'  # Указываем namespace для приложения pages

urlpatterns = [
    path('about/', views.about, name='about'),  # Имя маршрута: pages:about
    path('rules/', views.rules, name='rules'),  # Имя маршрута: pages:rules
]
