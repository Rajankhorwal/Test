"""authen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from userexm import views,view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='register'),
    path('login',views.loginPage,name='login'),
    path('logout',views.logoutuser,name='logout'),
    # path('website',views.next,name='next'),

    path('website', view.index, name='next'),
    # path('action', views.func,name='func'),
    path('action1', view.func1, name='func1'),
    path('action3', view.func3, name='func3'),
    path('action2', view.func2, name='func2')
]
