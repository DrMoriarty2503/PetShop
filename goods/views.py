from django.shortcuts import render

from goods.models import Popug

def catalog(request):
    popug = Popug.objects.all()

    context = {
        'popug': popug
    }

    return render(request, 'goods/catalog.html', context)

from django.shortcuts import render, redirect

from .models import Cart, Popug

def add_to_cart(request):
    if request.method == 'POST' and request.user.is_authenticated:
        product_id = request.POST.get('product_id')
        product = Popug.objects.get(id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart.goods.add(product)

        return redirect('main:index')  # Замените 'index' на имя вашего шаблона index.html
    else:
        return redirect('login')  # Замените 'login' на имя вашего шаблона для входа в систему

