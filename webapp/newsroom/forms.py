from django import forms
from django.contrib.auth.models import User

from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_body', 'news_author', 'news_publisher', 'news_date']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
