from rest_framework import serializers
from .models import Blogger, Blog, Images, Blogs


class Blogger_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blogger
        fields = '__all__'


class Blog_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'


class Blogs_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


# class Blogs_Serializer(serializers.Serializer):
    # Blogger = serializers.SerializerMethodField()
    # blog = serializers.SerializerMethodField()
    # images = serializers.SerializerMethodField()

    # class Meta:
    #     model = Blogs
    #     fields = (
    #         'blog',
    #     )

        # def get_Blogger(self, obj):
        #     return Blogger_Serializer(obj)

    # def get_blog(self, obj):
    #     return Blog_Serializer(obj)

        # def get_images(self, obj):
        #     return Images_Serializer(obj.images.all(), many=True)
