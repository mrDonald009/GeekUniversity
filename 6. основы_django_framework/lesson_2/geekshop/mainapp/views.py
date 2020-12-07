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

