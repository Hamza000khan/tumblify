from rest_framework import generics
from api import serializers
from django.contrib.auth.models import User
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]
    # Creation of blog for authenticated User

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
        return JsonResponse({'Message': serializer.data}, safe=False, status=status.HTTP_200_OK)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# class Update_Blog(generics.RetrieveUpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = serializers.BlogSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     # Update of blog for authenticated User
#     def perform_update(self, serializer):
#         serializer.save(added_by=self.request.user)
#         return JsonResponse({'Message': serializer.data}, safe=False, status=status.HTTP_200_OK)


# class BlogList(generics.ListCreateAPIView):
#     # queryset = Blog.objects.all()
#     # serializer_class = serializers.BlogSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     # Retrieving all the blogs for one specific User
#     def get(self, request):
#         if (request.user.id):
#             blogs = Blog.objects.filter(added_by=request.user.id)
#             serializer = BlogSerializer(blogs, many=True)

#             return JsonResponse({'Blogs': serializer.data}, safe=False, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse({'Blogs': 'Not Found'}, safe=False, status=status.HTTP_200_OK)


# class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
#     # queryset = Blog.objects.all()
#     # serializer_class = serializers.BlogSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

#     # Retrieving specific blog for authenticated User
#     def get(self, request, pk):
#         if (request.user.id):
#             blogs = Blog.objects.filter(added_by=request.user.id)
#             blog = blogs.filter(id=pk)
#             serializer = BlogSerializer(blog, many=True)
#             return JsonResponse({'Blogs': serializer.data}, safe=False, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse({'Blogs': 'Not Found'}, safe=False, status=status.HTTP_200_OK)


# class BlogDelete(generics.RetrieveDestroyAPIView):
#     # queryset = Blog.objects.all()
#     # serializer_class = serializers.BlogSerializer
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
