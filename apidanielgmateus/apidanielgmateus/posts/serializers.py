from rest_framework.serializers import ModelSerializer

from .models import Post, Category


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'name', 
            'description_short', 
            'content', 
            'cover_image',
            'slug'
        )


class PostCategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class PostsCategorySerializer(ModelSerializer):

    posts = PostSerializer(many=True)

    class Meta:
        model = Category
        fields = (
            'name',
            'slug',
            'posts'
        )
