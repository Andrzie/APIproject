
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import ApiView
from blog.models import Blog
from api.serializers import UserSerializer, BlogSerializer


class UserViewSet(viewsets.ModelViewSet):    # описывают поведение view
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BlogApiView(APIView):
    def get(self, request):
        blog = Blog.objects.all()
        return Response({'blog': BlogSerializer(blog, many=True).data})


class PostAPIView(APIView):
        def get(self, request):
            return Response({'title': 'Anton'})

        def post(self, request):
            return Response({'title': 'Ivan'})