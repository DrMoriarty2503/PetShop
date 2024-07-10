from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('order-form/', views.order_form, name='order-form'),
    path('order/',  views.order, name = 'order'),
    path('carts/', views.carts, name = 'carts')
]