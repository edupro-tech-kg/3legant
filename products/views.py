from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Category, Brand
from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .selectors import get_active_products, get_product_by_id, get_products_by_category, get_new_products, get_popular_products


class ProductListView(APIView):
    def get(self, request):
        qs = get_active_products()

        page = int(request.query_params.get("page", 1))
        limit = min(int(request.query_params.get("limit", 20)), 50)
        offset = (page - 1) * limit

        total = qs.count()
        products = qs[offset: offset + limit]

        serializer = ProductSerializer(products, many=True)

        return Response(
            {
                "data": serializer.data,
                "meta": {
                    "total": total,
                    "page": page,
                    "limit": limit,
                },
            },
            status=status.HTTP_200_OK,
        )


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BrandListView(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = get_product_by_id(product_id)
        if not product:
            return Response(
                {"detail": "Product not found"},
                status=404
            )

        serializer = ProductSerializer(product)
        return Response(serializer.data)

class ProductByCategoryView(APIView):
    def get(self, request, category_id):
        products = get_products_by_category(category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductByBrandView(APIView):
    def get(self, request, brand_id):
        products = get_products_by_category(brand_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class NewProductView(APIView):
    def get(self, request):
        products = get_new_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class PopularProductView(APIView):
    def get(self, request):
        products = get_popular_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)