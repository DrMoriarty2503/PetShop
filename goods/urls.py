from django.urls import path, include
from . import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name = 'index'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('main/', include('main.urls')),
    path('users/', include('users.urls', namespace='users')),

]