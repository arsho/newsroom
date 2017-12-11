from django.conf.urls import url
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

#app_name = 'newsroom'

urlpatterns = [
    url(r'^$', views.api_root, name='main_root'),
    url(r'^news/$',views.NewsList.as_view(), name='news-list'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.NewsDetail.as_view(), name='news-detail'),
    url(r'^news/(?P<pk>[0-9]+)/html/$', views.NewsHtml.as_view(), name='news-detail-html'),
    url(r'^users/$', views.UserList.as_view(), name = 'user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail')
]



urlpatterns = format_suffix_patterns(urlpatterns)


# urlpatterns = [
#     url(r'^$', views.index, name='index'),
#     url(r'^register_user/$', views.register_user, name='register_user'),
#     url(r'^login_user/$', views.login_user, name='login_user'),
#     url(r'^logout_user/$', views.logout_user, name='logout_user'),
#     url(r'^add_news/$', views.add_news, name='add_news'),
#     url(r'^edit_news/(?P<pk>[0-9]+)$', views.edit_news, name='edit_news'),
#     url(r'^delete_news/$', views.delete_news, name='delete_news'),
#     url(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail')
# ]