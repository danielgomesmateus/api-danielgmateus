from .models import Post, Category

from .serializers import CategorySerializer, PostsCategorySerializer, PostSerializer

from rest_framework.viewsets import ModelViewSet


class PostView(ModelViewSet):
    queryset = Post.objects.filter(status=True)
    serializer_class = PostSerializer
    http_method_names = ['get']
    lookup_field = 'slug'


class CategoryView(ModelViewSet):
    queryset = Category.objects.filter(status=True, posts__status=True)
    default_serializer_class = CategorySerializer
    serializer_classes = {
        'list': CategorySerializer,
        'retrieve': PostsCategorySerializer
    }
    http_method_names = ['get']
    lookup_field = 'slug'

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)

