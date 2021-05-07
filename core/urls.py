"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from rest_framework.routers import DefaultRouter

from api import views as api_views
from utils.auth_views import register

admin.site.site_title = '咖啡店 網站管理'
admin.site.site_header = '咖啡店 管理'

login_params = {
    'template_name': 'users/login.html',
    'redirect_authenticated_user': True,
}

password_reset_params = {
    'template_name': 'users/password_reset.html',
    'email_template_name': 'users/password_reset/email.html',
    'subject_template_name': 'users/password_reset/subject.txt',
    'success_url': reverse_lazy('login'),
}

password_set_params = {
    'template_name': 'users/password_set.html',
    'post_reset_login': True,
    'success_url': reverse_lazy('login'),
}

router = DefaultRouter()
router.register('coffees', api_views.CoffeeViewSet)

urlpatterns = [
    path('', lambda request: redirect('coffees:index'), name='root'),
    path('login/', LoginView.as_view(**login_params), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path(
        'password-reset/',
        PasswordResetView.as_view(**password_reset_params),
        name='password_reset',
    ),
    path(
        'password-set/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(**password_set_params),
        name='password_set',
    ),

    path('coffees/', include('coffees.urls')),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
