from .models import Blog
from api import serializers
from rest_framework import status
from rest_framework import generics
from django.http import JsonResponse
from rest_framework import permissions
from .serializers import BlogSerializer
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    # Listing ALL Users
    queryset: object = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    # Listing specific user details
    queryset: object = User.objects.all()
    serializer_class = serializers.UserSerializer


class BlogList(generics.ListCreateAPIView):
    # Retrieving all blogs only for authenticated user and serializing data
    queryset: object = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer) -> object:
        serializer: dict
        user: int

        user = self.request.user
        # Creation of blog for authenticated User
        serializer.save(added_by=user)
        return JsonResponse({'Message': serializer.data}, safe=False, status=status.HTTP_200_OK)


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    # Retrieving specific blogs for authenticated user and managing crud with generic views from DRF
    queryset: dict = Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
