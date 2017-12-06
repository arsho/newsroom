from django import forms
from django.contrib.auth.models import User

from .models import News
import datetime
AUTHOR_CHOICES = [
    ('BBC', 'BBC'),
    ('CNN', 'CNN'),
    ('AL JAZEERA','AL JAZEERA'),
    ('RUSSIA TODAY', 'RUSSIA TODAY')
]

class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    news_author = forms.CharField(widget = forms.Select(choices=AUTHOR_CHOICES))
    news_date = forms.DateField(initial=datetime.date.today)
    forms.DateInput.input_type = "date"

    def clean_news_date(self):
        date_value = self.cleaned_data['news_date']
        if date_value > datetime.date.today():
            raise forms.ValidationError('The date cannot be in the future!')
        return date_value

    class Meta:
        model = News
        fields = ['news_title', 'news_body', 'news_author', 'news_date']


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
