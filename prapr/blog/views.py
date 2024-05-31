from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, LoginForm, BlogForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Blog
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404,redirect


# Create your views here.
def home(request):
    blogs = Blog.objects.all()
    return render(request,'blog/home.html',{'blogs':blogs})

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,"CONGRATULATION, You are Registered!")
            user = form.save()
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
    else:
        form=SignUpForm()
    return render(request,'blog/signup.html',{'form':form})

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request = request, data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                pwd = form.cleaned_data['password']
                user = authenticate(username=uname, password=pwd)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def dashboard(request):
    if request.user.is_authenticated:
        blogs = Blog.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'blog/dashboard.html',{'blogs':blogs,'full_name':full_name,'groups':gps})

def add_blog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = BlogForm(request.POST, request.FILES)  # Include request.FILES for handling file uploads
            if form.is_valid():
                # Save all form fields into the Blog model instance
                blg = form.save(commit=False)  # Don't commit to the database yet
                blg.save()  # Now save to the database
                return HttpResponseRedirect('/')  # Redirect to home page after successfully adding blog
        else:
            form = BlogForm()
        return render(request, 'blog/addblog.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')

def update_blog(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            form = BlogForm(request.POST,instance = pi)
            if form.is_valid():
                form.save()
        else:
            pi = Blog.objects.get(pk=id)
            form = BlogForm(instance=pi)
        return render(request, 'blog/updateblog.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')

def delete_blog(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Blog.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def blog_detail(request, pk):
    blog_post = get_object_or_404(Blog, pk=pk)
    return render(request, 'blog/blog_detail.html', {'blog': blog_post})

# blog/views.py
from django.shortcuts import render


def contact_submit(request):
    if request.method == 'POST':
        # handle form submission
        return HttpResponse("Form submitted successfully")
    return HttpResponse("Invalid request")
