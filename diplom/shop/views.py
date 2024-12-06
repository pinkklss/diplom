from django.shortcuts import render, redirect
from .forms import ProductForm, OrderForm, OrderItemForm


def create_order(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)
        if order_form.is_valid() and order_item_form.is_valid():
            order = order_form.save()  # Сохраняем новый заказ
            order_item = order_item_form.save(commit=False)  # Не сохраняем в базу данных сразу
            order_item.order = order  # Присваиваем элементу заказа созданный заказ
            order_item.save()  # Теперь сохраняем элемент заказа
            return redirect('order_success')  # Перенаправление на страницу успешного создания заказа
    else:
        order_form = OrderForm()
        order_item_form = OrderItemForm()

    return render(request, 'create_order.html', {
        'order_form': order_form,
        'order_item_form': order_item_form,
    })


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:
        form = ProductForm()

    return render(request, 'product_list.html', {'form': form})


