from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/products.html')

def test_context(request):
    context = {
        'title': 'добро пожаловать!',
        'username': 'Ivan Ivanovich',
        'products': [
            {'name': 'Черное худи', 'price': '2 999 руб.'},
            {'name': 'Джинсы', 'price': '5800 руб.'}
        ],
        'promotion': True,
        'promotion_products': [
            {'name': 'Туфли Dr Martnes', 'price': '10 000 руб.'},
        ],
    }

    products = context['products']
    return render(request, 'mainapp/context.html', context)

def test_product_context(request):
    context = {
        'title': 'Привет!',
        'user_name': 'Ivan',
        'goods': [
            {'name': 'Синяя куртка The North Fac', 'price': '23 725,00 руб.'},
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.'},
            {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.'}
        ],
    }

    goods = context['goods']
    return render(request, 'mainapp/products_context.html', context)