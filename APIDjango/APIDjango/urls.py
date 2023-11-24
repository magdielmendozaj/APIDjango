"""APIDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path, include
from api.views import login_view, register_view, index_view, logout_view, GitHubCallback, GitHubLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('login/',login_view, name='login'),
    path('signup/',register_view, name='signup'),
    path('index',index_view, name='index'),
    path('logout/',logout_view, name='logout'),
    path('github/login/', GitHubLogin.as_view(), name='github-login'),
    path('github/callback/', GitHubCallback.as_view(), name='github-callback'),
]
