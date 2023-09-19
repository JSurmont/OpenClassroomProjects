from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from shop.models import Category, Product, Article
from shop.permissions import IsAdminAuthenticated, IsStaffAuthenticated
from shop.serializers import ArticleSerializer, ProductListSerializer, ProductDetailSerializer, \
                                CategoryListSerializer, CategoryDetailSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class CategoryViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    def get_queryset(self):
        return Category.objects.filter(active=True)

    @action(detail=True, methods=['post', ])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class AdminCategoryViewset(MultipleSerializerMixin, ModelViewSet):

    serializer_class = CategoryListSerializer
    detail_serializer_class = CategoryDetailSerializer

    permission_classes = [IsAdminAuthenticated, IsStaffAuthenticated]

    queryset = Category.objects.all()


class ProductViewset(MultipleSerializerMixin, ReadOnlyModelViewSet):

    serializer_class = ProductListSerializer
    detail_serializer_class = ProductDetailSerializer

    def get_queryset(self):
        products = Product.objects.filter(active=True)
        category_id = self.request.GET.get('category_id')
        if category_id:
            products = products.filter(category_id=category_id)
        return products

    @action(detail=True, methods=['post', ])
    def disable(self, request, pk):
        self.get_object().disable()
        return Response()


class ArticleViewset(ReadOnlyModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        articles = Article.objects.filter(active=True)
        product_id = self.request.GET.get('product_id')
        if product_id:
            articles = articles.filter(product_id=product_id)
        return articles


class AdminArticleViewset(ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
