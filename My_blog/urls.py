"""My_blog URL Configuration

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
from django.urls import path
from user import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signupuser, name='signupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('blog/', views.blog, name='blog'),
    path('MyBlogs/', views.list_blogs, name='MyBlogs'),
    path('AllBlogs/', views.all_blogs, name='AllBlogs'),
    path('Blog/<blog_id>/', views.details, name='details'),
    path('Blog/<blog_id>/update', views.update, name='update'),
    path('Blog/<blog_id>/delete', views.delete, name='delete'),
    ]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
