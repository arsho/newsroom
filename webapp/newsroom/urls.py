from django.conf.urls import url

from . import views

app_name = 'newsroom'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register_user/$', views.register_user, name='register_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^add_news/$', views.add_news, name='add_news'),
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail')
]