from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny

from .selectors import search_products, suggest_products
from .serializers import SearchProductSerializer, SuggestSerializer


class ProductSearchView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "").strip()
        if not query:
            return Response(
                {"data": [], "meta": {"total": 0, "page": 1, "limit": 20}},
                status=status.HTTP_200_OK,
            )

        page = int(request.query_params.get("page", 1))
        limit = min(int(request.query_params.get("limit", 20)), 50)
        offset = (page - 1) * limit

        results, total = search_products(query=query, limit=limit, offset=offset)
        serializer = SearchProductSerializer(results, many=True)

        return Response(
            {
                "data": serializer.data,
                "meta": {"total": total, "page": page, "limit": limit},
            },
            status=status.HTTP_200_OK,
        )


class ProductSuggestView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        query = request.query_params.get("q", "").strip()
        if not query:
            return Response({"suggestions": []}, status=status.HTTP_200_OK)

        limit = min(int(request.query_params.get("limit", 10)), 20)
        suggestions = suggest_products(query=query, limit=limit)

        serializer = SuggestSerializer([{"value": s} for s in suggestions], many=True)

        return Response({"suggestions": serializer.data}, status=status.HTTP_200_OK)

