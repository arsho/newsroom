# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .forms import NewsForm, UserForm
from .models import News


def index(request):
    news_list = News.objects.all()
    if not request.user.is_authenticated():
        return render(request, 'newsroom/index_visitor.html', {'news_list': news_list})
    else:
        return render(request, 'newsroom/index.html', {'news_list': news_list})


# @login_required
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
                message = 'Successfully logged in'
                messages.success(request, message)
                return HttpResponseRedirect(reverse('newsroom:index'))
            else:
                message = 'Account is disabled'
                messages.error(request, message)
        else:
            message = 'Wrong username or password'
            messages.error(request, message)
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
                return HttpResponseRedirect(reverse('newsroom:index'))
                # news_list = News.objects.filter(news_publisher=request.user)

    context = {
        'form': form
    }
    return render(request, 'newsroom/register.html', context)


def add_news(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('newsroom:login_user'))
    else:
        form = NewsForm(request.POST or None)
        if form.is_valid():
            news = form.save(commit=False)
            news.news_publisher = request.user
            news.save()
            message = 'News is saved successfully'
            messages.success(request, message)
            return HttpResponseRedirect(reverse('newsroom:index'))
        context = {
            "form": form,
            'page_type': 'Add'
        }
        return render(request, 'newsroom/add_edit_news.html', context)


def edit_news(request, pk):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('newsroom:login_user'))
    else:
        existing_news = get_object_or_404(News, pk=pk)
        if existing_news.news_publisher != request.user:
            message = 'You do not have permission to edit this news'
            messages.error(request, message)
            return HttpResponseRedirect(reverse('newsroom:index'))
        else:
            form = NewsForm(request.POST or None, instance=existing_news)
            if request.method == 'POST':
                if form.is_valid():
                    news = form.save(commit=False)
                    news.news_publisher = request.user
                    news.save()
                    message = 'News is updated successfully'
                    messages.success(request, message)
                    return HttpResponseRedirect(reverse('newsroom:index'))
                else:
                    message = 'Form is not valid'
                    messages.error(request, message)
            context = {'form': form, 'page_type': 'edit'}
            return render(request, 'newsroom/add_edit_news.html', context)


def delete_news(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('newsroom:login_user'))
    else:
        if request.method == 'POST':
            id = request.POST.get('delete_news_id', None)
            try:
                existing_news = News.objects.get(id=id)
                if request.user == existing_news.news_publisher:
                    existing_news.delete()
                    messages.success(request, 'Deletion of the selected news is successful')
                    return HttpResponseRedirect(reverse('newsroom:index'))
                else:
                    error_message = 'You do not have the permission to delete this'
                    messages.error(request, error_message)
                    return HttpResponseRedirect(reverse('newsroom:index'))
            except:
                error_message = 'The news does not exist'
                messages.error(request, error_message)
                return HttpResponseRedirect(reverse('newsroom:index'))


def detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    if not request.user.is_authenticated():
        return render(request, 'newsroom/detail_visitor.html', {'news': news})
    else:
        return render(request, 'newsroom/detail.html', {'news': news})
