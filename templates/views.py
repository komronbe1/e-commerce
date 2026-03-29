from django.shortcuts import render, redirect
from .models import Product, Order
from django.db.models import Sum

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def create_order(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)

        Order.objects.create(
            user=request.user,
            price=product.price
        )

    return redirect('/orders/')


def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'orders.html', {'orders': orders})


def stats(request):
    total_orders = Order.objects.count()
    total_price = Order.objects.aggregate(total=Sum('price'))['total'] or 0

    return render(request, 'stats.html', {
        'total_orders': total_orders,
        'total_price': total_price
    })