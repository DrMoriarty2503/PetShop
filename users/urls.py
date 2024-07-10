from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.user_login, name='login'),  # Добавлен маршрут для представления входа в систему
    path('register/', views.register, name='register'),  # Добавлен маршрут для представления регистрации
    path('logout/', views.logout_view, name='logout'),  # Добавлен маршрут для представления выхода из системы
]
