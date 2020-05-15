"""Определяет схемы URL ля пользователей"""

from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'


urlpatterns = [
    # Страница входа
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    # Страница выхода
    path('logout/', views.logout_view, name='logout')
]
