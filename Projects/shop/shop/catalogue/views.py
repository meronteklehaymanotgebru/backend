from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem, Product
from .forms import ProductForm
from django.contrib.auth import logout

def list_products(request):
    # http request
    products=Product.objects.all()
    return render(request, "catalogue/products.html",{"products":products})

# template and querying
# forms listing/quering data
# api without serializer and  
# hosting witout heroku but use cloud infrastracture and how to choose cloud providers
# Conternization/Docker
# Orchestration/Kubernetes
# Site reliability engineering/monitoring, logging, scalability, metrics/how much CPU the application use
# Create a single object view

def product_detail(request,id):
   product=Product.objects.get(id=id)
   return render(request, "catalogue/product_detail.html", {"product": product})
    # what are we rendering is the request and the second argument is where


@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Add request.FILES here
        if form.is_valid():
            form.save()
            return redirect('list_products')
    else:
        form = ProductForm()
    return render(request, 'catalogue/product_form.html', {'form': form})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total = cart.get_total_price()
    return render(request, 'cart/detail.html', {'items': items, 'total': total})

@login_required
def remove_from_cart(request, product_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def logout_confirm_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login') 
    return render(request, 'registration/logout.html')