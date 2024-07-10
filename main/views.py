from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Popug
from goods.models import Cart
from .models import Req




def index(request):
    popug = Popug.objects.all()
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user)
        cart = user_cart.first().goods.all() if user_cart.exists() else []
        context = {
            'popug': popug,
            'cart': cart
        }
        return render(request, 'main/index.html', context)
    else:
        context = {
            'popug': popug
        }
        return render(request, 'main/index.html', context)


from .forms import ReqForm


from .forms import ReqForm
from django.shortcuts import render, redirect

def order_form(request):
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user  # Привязываем пользователя к заявке
            form.save()  # Сохраняем данные формы в базе данных
            return redirect('main:index')  # Перенаправляем пользователя на страницу успешного завершения
    else:
        form = ReqForm()

    context = {
        'form': form
    }
    return render(request, 'main/order_form.html', context)

def order(request):
    user = request.user  # Получаем текущего пользователя
    user_requests = Req.objects.filter(user=user)  # Фильтруем заявки по пользователю
    return render(request, 'main/order.html', {'user_requests': user_requests})


from django.db.models import Sum



def carts(request):
    popug = Popug.objects.all()
    if request.user.is_authenticated:
        user_cart = Cart.objects.filter(user=request.user)
        cart = user_cart.first().goods.all() if user_cart.exists() else []
        total_price = cart.aggregate(total=Sum('price'))['total']
        context = {
            'popug': popug,
            'cart': cart,
            'total_price': total_price
        }
        return render(request, 'main/carts.html', context)




