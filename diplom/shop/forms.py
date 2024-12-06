from django import forms
from .models import Shop, Product, Category, Order, OrderItem


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name', 'url', 'user', 'state']
        labels = {
            'name': 'Название магазина',
            'url': 'Ссылка на магазин',
            'user': 'Пользователь',
            'state': 'Статус получения заказов',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
            'state': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity_in_stock']
        labels = {
            'name': 'Название товара',
            'description': 'Описание',
            'price': 'Цена',
            'quantity_in_stock': 'Количество в наличии',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'quantity_in_stock': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'shops']
        labels = {
            'name': 'Название категории',
            'shops': 'Магазины',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'shops': forms.CheckboxSelectMultiple(),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'state', 'contact']
        widgets = {
            'dt': forms.HiddenInput(),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['order', 'product', 'quantity']