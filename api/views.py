from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [IsOwnerOrReadOnly]

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .serializers import Blog_Serializer, Blogger_Serializer, Blogs_Serializer, Images_Serializer
# from .models import Blog, Blogs, Images, Blogger
# from rest_framework import status
# import json
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.http import Http404
# from rest_framework import generics

# # @csrf_exempt
# # @permission_classes([IsAuthenticated])


# class BlogList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         user = request.user.id
#         blogs = Blog.objects.filter(added_by=user)
#         images = Images.objects.filter(blog=user)
#         serializer = Blog_Serializer(blogs, many=True)
#         ImagesSerializer = Images_Serializer(images, many=True)

#         return JsonResponse({'Blogs': serializer.data, 'images': ImagesSerializer.data}, safe=False, status=status.HTTP_200_OK)

#     def post(self, request, format=None):
#         serializer = Blogs_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BlogListDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     # queryset = Blogs.objects.all()
#     # serializer_class = Blogs_Serializer
#     # lookup_fields = []
#     # serializer_class = Blog_Serializer

#     def get(self, request, pk):
#         user = request.user.id
#         blogs = Blog.objects.filter(id=pk)
#         images = Images.objects.filter(blog=pk)
#         serializer = Blog_Serializer(blogs, many=True)
#         ImagesSerializer = Images_Serializer(images, many=True)

#         return JsonResponse({'Blogs': serializer.data, 'images': ImagesSerializer.data}, safe=False, status=status.HTTP_200_OK)

#     # def post(self, request, format=None):
#     #     serializer = Blogs_Serializer(data=request.data)
#     #     if serializer.is_valid():
#     #         serializer.save()

#     #         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
