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
from api.views import login_view, register_view, index_view, logout_view
# from allauth.socialaccount.views import OAuth2View
# from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
# from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount import views as allauth_socialaccount_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view),
    path('login/',login_view, name='login'),
    path('signup/',register_view, name='signup'),
    path('index',index_view, name='index'),
    path('logout/',logout_view, name='logout'),
    # re_path('accounts/github/login/callback/', OAuth2View.as_view(adapter_class=GitHubOAuth2Adapter, client_class=OAuth2Client), name='socialaccount_callback'),
    path('accounts/', include('allauth.socialaccount.urls')),
    path('accounts/github/login/callback/', allauth_socialaccount_views.github_login_callback, name='github_login_callback'),
]
