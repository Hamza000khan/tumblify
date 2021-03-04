from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = ['bookmark',
                  'quote',
                  'image_embed',
                  'video_embed',
                  'gist_embed',
                  'user',
                  'created_date']


class UserSerializer(serializers.ModelSerializer):
    blog = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Setting read_only=True, the posts field has write access by default.

    class Meta:
        model = User
        fields = ['id', 'username', 'blog']
