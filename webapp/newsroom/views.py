# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.urls import reverse

from .forms import NewsForm, UserForm
from .models import News


# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'newsroom/login.html')
    else:
        news_list = News.objects.all()
        return render(request, 'newsroom/index.html', {'news_list': news_list})


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'newsroom/login.html', context)


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                news_list = News.objects.filter(news_publisher=request.user)
                return render(request, 'newsroom/index.html', {'news_list': news_list})
            else:
                return render(request, 'newsroom/login.html', {'error_message': 'Account is disabled'})
    return render(request, 'newsroom/login.html')


def register_user(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                news_list = News.objects.filter(news_publisher=request.user)
                return render(request, 'newsroom/index.html', {'news_list': news_list})

    context = {
        'form': form
    }
    return render(request, 'newsroom/register.html', context)


def add_news(request):
    if not request.user.is_authenticated():
        return render(request, 'newsroom/login.html')
    else:
        form = NewsForm(request.POST or None)
        if form.is_valid():
            news = form.save(commit=False)
            news.news_publisher = request.user
            news.save()
            return HttpResponseRedirect(reverse('newsroom:index'))
        context = {
            "form": form
        }
        return render(request, 'newsroom/add_news.html', context)


def detail(request, pk):
    if not request.user.is_authenticated():
        return render(request, 'newsroom/login.html')
    else:
        news = get_object_or_404(News, pk=pk)
        return render(request, 'newsroom/detail.html', {'news': news})
