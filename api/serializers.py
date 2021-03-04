from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    Blogger = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    Blog = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Blog.objects.all())

    class Meta:
        model = User
        fields = '__all__'


# from rest_framework import serializers
# from .models import Blogger, Blog, Images, Blogs


# class Blogger_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Blogger
#         fields = '__all__'


# class AttrPKField(serializers.PrimaryKeyRelatedField):
#     def get_queryset(self):
#         user = self.context['request'].user.id
#         print(user)
#         queryset = Blog.objects.filter(user=user)
#         return queryset


# class Blog_Serializer(serializers.ModelSerializer):

#     class Meta:
#         model = Blog
#         fields = '__all__'


# class Images_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Images
#         fields = '__all__'


# class Blogs_Serializer(serializers.ModelSerializer):
#     blog = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Blog.objects.all())

#     class Meta:
#         model = Blogs
#         fields = '__all__'

#         # extra_fields = ['Bookmark']
#         # exclude = (['images'])
