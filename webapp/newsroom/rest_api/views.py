# Fifth attempt
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from django.contrib.auth.models import User

from ..models import News
from .serializers import NewsSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

<<<<<<< Updated upstream
=======
@api_view(['GET'])
def api_index(request, format=None):
    return Response({
        'news_list': reverse('news-list', request=request, format=format),
        'user_list': reverse('user-list', request=request, format=format),
    })
>>>>>>> Stashed changes

class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(news_publisher=self.request.user)


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'news_list': reverse('news-list', request=request, format=format),
        'user_list': reverse('user-list', request=request, format=format),
    })

class NewsHtml(generics.GenericAPIView):
    queryset = News.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        news = self.get_object()
        return Response(news)

    # Fourth Attempt: Using Mixins
    # from rest_framework import mixins
    # from rest_framework import generics
    #
    # from .models import News
    # from .serializers import NewsSerializer
    #
    # class NewsList(mixins.ListModelMixin,
    #                mixins.CreateModelMixin,
    #                generics.GenericAPIView):
    #     queryset = News.objects.all()
    #     serializer_class = NewsSerializer
    #
    #     def get(self, request, *args, **kwargs):
    #         return self.list(request, *args, **kwargs)
    #
    #     def post(self, request, *args, **kwargs):
    #         return self.create(self, *args, **kwargs)
    #
    # class NewsDetail(mixins.RetrieveModelMixin,
    #                  mixins.UpdateModelMixin,
    #                  mixins.DestroyModelMixin,
    #                  generics.GenericAPIView):
    #     queryset = News.objects.all()
    #     serializer_class = NewsSerializer
    #
    #     def get(self, request, *args, **kwargs):
    #         return self.retrieve(request, *args, **kwargs)
    #
    #     def put(self, request, *args, **kwargs):
    #         return self.update(request, *args, **kwargs)
    #
    #     def delete(self, request, *args, **kwargs):
    #         return self.destroy(request,*args, **kwargs)

    # Third Attempt: Class based views
    # from django.http import Http404
    # from rest_framework.views import APIView
    # from rest_framework.response import Response
    # from rest_framework import status
    #
    # from .models import News
    # from .serializers import NewsSerializer
    #
    # class NewsList(APIView):
    #     def get(self, request, format = None):
    #         news = News.objects.all()
    #         serializer = NewsSerializer(news, many=True)
    #         return Response(serializer.data)
    #
    #     def post(self, request, format = None):
    #         serializer = NewsSerializer(data = request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data,
    #                             status = status.HTTP_201_CREATED)
    #
    # class NewsDetail(APIView):
    #     def get_object(self, pk):
    #         try:
    #             return News.objects.get(pk = pk)
    #         except News.DoesNotExist:
    #             raise Http404
    #
    #     def get(self, request, pk, format=None):
    #         news = self.get_object(pk)
    #         serializer = NewsSerializer(news)
    #         return Response(serializer.data)
    #
    #     def put(self, requst, pk, format = None):
    #         news = self.get_object(pk)
    #         serializer = NewsSerializer(news, data = requst.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     def delete(self, request, pk, format = None):
    #         news = self.get_object(pk)
    #         news.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)

    # Second Attempt: Requests and Responses
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status
    #
    #
    # from .models import News
    # from .serializers import NewsSerializer
    #
    # @api_view(['GET', 'POST'])
    # def news_list(request, format = None):
    #     if request.method == 'GET':
    #         news = News.objects.all()
    #         serializer = NewsSerializer(news, many=True)
    #         return Response(serializer.data)
    #
    #     elif request.method == 'POST':
    #         serializer = NewsSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data,
    #                             status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    # @api_view(['GET', 'DELETE', 'PUT'])
    # def news_detail(request, pk, format = None):
    #     try:
    #         news = News.objects.get(pk = pk)
    #     except News.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     if request.method == 'GET':
    #         serializer = NewsSerializer(news)
    #         return Response(serializer.data)
    #     elif request.method == 'PUT':
    #         serializer = NewsSerializer(news, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors,
    #                         status = status.HTTP_400_BAD_REQUEST)
    #     elif request.method == 'DELETE':
    #         news.delete()
    #         return Response(status = status.HTTP_204_NO_CONTENT)

    # First attempt using JSON response
    # from rest_framework.generics import ListCreateAPIView, \
    #     RetrieveUpdateDestroyAPIView
    # from rest_framework.permissions import IsAuthenticated
    # from django.http import HttpResponse, JsonResponse
    # from django.views.decorators.csrf import csrf_exempt
    # from rest_framework.renderers import JSONRenderer
    # from rest_framework.parsers import JSONParser
    # from .models import News
    # from .serializers import NewsSerializer
    # @csrf_exempt
    # def news_list(request):
    #     if request.method == 'GET':
    #         news_list = News.objects.all()
    #         serializer = NewsSerializer(news_list, many=True)
    #         return JsonResponse(serializer.data, safe=False)
    #
    #     elif request.method=='POST':
    #         data = JSONParser().parse(request)
    #         serializer = News(data = data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data, status=201)
    #         return JsonResponse(serializer.errors, status=400)
    #
    # @csrf_exempt
    # def news_detail(request, pk):
    #     try:
    #         news = News.objects.get(pk=pk)
    #     except News.DoesNotExist:
    #         return HttpResponse(status=404)
    #
    #     if request.method == 'GET':
    #         serializer = NewsSerializer(news)
    #         return JsonResponse(serializer.data)
    #     elif request.method == 'PUT':
    #         data = JSONParser().parse(request)
    #         serializer = NewsSerializer(news, data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=400)
    #     elif request.method=='DELETE':
    #         news.delete()
    #         return HttpResponse(status=204)
