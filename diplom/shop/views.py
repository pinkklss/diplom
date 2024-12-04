from django.shortcuts import render, redirect
from .models import Order, OrderItem, Payment
from .forms import OrderForm, OrderItemForm
from django.contrib.auth.decorators import login_required


@login_required
def create_order(request):
    if request.method == 'POST':
        order = Order.objects.create(user=request.user)
        for item in request.POST.getlist('order_items'):
            product_id, quantity = item.split(',')
            product = Product.objects.get(id=product_id)
            order_item = OrderItem(order=order, product=product, quantity=quantity)
            order_item.save()
            order.total_price += product.price * quantity
        order.save()
        return redirect('order_detail', order_id=order.id)

    products = Product.objects.all()
    return render(request, 'create_order.html', {'products': products})


@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'order_detail.html', {'order': order})


@login_required
def process_payment(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    if request.method == 'POST':
        # В этом месте реальная логика обработки платежа
        payment = Payment.objects.create(order=order, amount=order.total_price, status='Completed')
        return redirect('order_detail', order_id=order.id)

    return render(request, 'process_payment.html', {'order': order})


