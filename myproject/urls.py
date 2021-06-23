"""myproject URL Configuration

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

from account import views as account
from django.contrib import admin
from django.urls import path
from board import views as blog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.home, name="home"),
    path('blog/<int:id>', blog.post_read, name="post_read"),
    path('blog/new', blog.post_create, name="post_create"),
    path('blog/edit/<int:id>', blog.post_edit, name="post_edit"),
    path('blog/delete/<int:id>', blog.post_delete, name="post_delete"),
    path('blog/comment_create/<int:id>', blog.comment_create, name="comment_create"),
    path('account/signup', account.signup_view, name="signup"),
    path('account/login', account.login_view, name = "login"),
    path('account/logout', account.logout_view, name = "logout"),
]
