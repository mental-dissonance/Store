from django.shortcuts import render
from .models import Products
from .models import Categories
from django.views.generic import DetailView

def index(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    return render(request, "main/index.html", {'products': products, 'categories': categories})
   
def phones(request):
    products = Products.objects.all()
    cat = 'Смартфоны'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})

def notes(request):
    products = Products.objects.all()
    cat = 'Ноутбуки'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})
    
def computers(request):
    products = Products.objects.all()
    cat = 'Компьютеры'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})

def tvs(request):
    products = Products.objects.all()
    cat = 'Телевизоры'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})

def tablets(request):
    products = Products.objects.all()
    cat = 'Планшеты'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})

def columns(request):
    products = Products.objects.all()
    cat = 'Колонки'
    return render(request, "main/catalog.html", {'products': products, 'cat':cat})

class ProductDetailView(DetailView):
    model = Products
    cat = Products.category
    template_name = 'main/product.html'
    context_object_name = 'product'
    
    def Cat(self):
        cat = self.category
        return cat
    
def busket(request):
    
    return render(request, 'main/busket.html')