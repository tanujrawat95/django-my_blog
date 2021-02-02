from django.shortcuts import render, redirect , get_object_or_404 , HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout,authenticate
from .forms import BlogForm
from .models import Blog

def signupuser(request):
    if request.method == "GET":
        return render(request, 'user/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('blog')
            except IntegrityError:
                return render(request, 'user/signupuser.html', {'form': UserCreationForm(), 'error':'Username already exists'})
        else:
            return render(request, 'user/signupuser.html', {'form': UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == "GET":
        return render(request, 'user/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'user/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request,user)
            return redirect('blog')

def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect('signupuser')


def blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            new_blog=form.save(commit=False)
            new_blog.user = request.user
            new_blog.save()
            return redirect ('MyBlogs')
    else:
        form = BlogForm()
    return render(request, 'user/blog.html', {'form': form})


def list_blogs(request):
    current = Blog.objects.filter(user=request.user).order_by("-created")
    return render(request,'user/your_blogs.html',{'current':current})

def all_blogs(request):
    current = Blog.objects.all().order_by("-created")
    return render(request,'user/all_blogs.html',{'current':current})

def details(request, blog_id):
    current = get_object_or_404(Blog, pk=blog_id)
    return render(request,'user/details.html',{'current':current})

def update(request, blog_id):
    current = get_object_or_404(Blog, pk = blog_id)
    if request.method == "GET":
        form = BlogForm(instance = current)
        return render(request, "user/update.html", {'form':form})
    else:
        form=BlogForm(request.POST, request.FILES, instance = current)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/Blog/"+blog_id)

def delete(request, blog_id):
    current = get_object_or_404(Blog, pk = blog_id)
    if request.method == "POST":
        current.delete()
        return redirect('MyBlogs')
