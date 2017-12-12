# Second attempt: Hyperlinked model serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import News


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    news_publisher = serializers.ReadOnlyField(source='news_publisher.username')

    class Meta:
        model = News
        fields = ('url', "id", "news_title", "news_body",
                  "news_author", "news_publisher", "news_date")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    news_list = serializers.HyperlinkedRelatedField(many=True,
                                                    view_name='news-detail',
                                                    read_only=True)

    class Meta:
        model = User
        fields = ('url','id', 'username', 'email', 'news_list')
# First Attempt: Model Serializer
# from django.contrib.auth.models import User
# from rest_framework import serializers
# from .models import News
#
# class NewsSerializer(serializers.ModelSerializer):
#     news_publisher = serializers.ReadOnlyField(source='news_publisher.username')
#     class Meta:
#         model = News
#         fields = ("id","news_title", "news_body",
#                   "news_author", "news_publisher", "news_date")
#
# class UserSerializer(serializers.ModelSerializer):
#     news_list = serializers.PrimaryKeyRelatedField(many=True,
#                                               queryset=News.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'news_list')
