from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .selectors import search_products, suggest_products
from .serializers import SearchProductSerializer
from .models import SearchQueryLog

class ProductSearchView(APIView):

    def get(self, request):
        q = request.query_params.get("q", "").strip()

        if not q:
            return Response(
                {"detail": "Query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        page = int(request.query_params.get("page", 1))
        limit = min(int(request.query_params.get("limit", 20)), 50)
        offset = (page - 1) * limit

        products, total = search_products(
            query=q,
            limit=limit,
            offset=offset,
        )

        serializer = SearchProductSerializer(products, many=True)

        SearchQueryLog.objects.create(
            query=q,
            results_count=total,
        )

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

class ProductSuggestView(APIView):

    def get(self, request):
        q = request.query_params.get("q", "").strip()

        suggestions = suggest_products(query=q)

        return Response(
            {"data": suggestions},
            status=status.HTTP_200_OK,
        )