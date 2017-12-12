from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^$', views.api_root, name='api_root'),
    url(r'^news/$', views.NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='news-detail'),
    url(r'^news/(?P<pk>[0-9]+)/html/$', views.NewsHtml.as_view(), name='news-detail-html'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
