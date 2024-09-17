from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('catalog/phones/', views.phones, name='Смартфоны'),
    path('catalog/notes/', views.notes, name='Ноутбуки'),
    path('catalog/computers/', views.computers, name='Компьютеры'),
    path('catalog/tvs/', views.tvs, name='Телевизоры'),
    path('catalog/tablets/', views.tablets, name='Планшеты'),
    path('catalog/columns/', views.columns, name='Колонки'),
    path('<int:pk>', views.ProductDetailView.as_view(), name='product'),
    path('busket', views.busket, name='Корзина'),
]