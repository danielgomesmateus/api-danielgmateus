from rest_framework.serializers import ModelSerializer

from .models import Post, Category


class PostCategoryListSerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class PostsCategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = (
            'name',
            'slug'
        )


class PostSerializer(ModelSerializer):

    category = PostsCategorySerializer()

    class Meta:
        model = Post
        fields = (
            'name',
            'description_short',
            'content',
            'cover_image',
            'slug',
            'created_at',
            'updated_at',
            'category'
        )

