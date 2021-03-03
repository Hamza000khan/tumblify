from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import Blog_Serializer, Blogger_Serializer, Blogs_Serializer, Images_Serializer
from .models import Blog, Blogs, Images
from rest_framework import status
import json


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_blogs(request):
    user = request.user.id
    blogs = Blog.objects.filter(added_by=user)
    images = Images.objects.all()
    serializer = Blog_Serializer(blogs, many=True)
    ImagesSerializer = Images_Serializer(images, many=True)
    return JsonResponse({'Blogs': serializer.data, 'images': ImagesSerializer.data}, safe=False, status=status.HTTP_200_OK)
