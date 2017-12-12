from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
<<<<<<< Updated upstream
    url(r'^$', views.api_root, name='api_root'),
=======
    url(r'^all/$', views.api_root, name='api_all'),
    url(r'^/$', views.api_index, name='api_index'),
>>>>>>> Stashed changes
    url(r'^news/$', views.NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='news-detail'),
    url(r'^news/(?P<pk>[0-9]+)/html/$', views.NewsHtml.as_view(), name='news-detail-html'),
    url(r'^users/$', views.UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)
