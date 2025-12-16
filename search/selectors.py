from django.db.models import F
from django.contrib.postgres.search import (SearchVector, SearchQuery, SearchRank,)
from apps.products.models import Product

def search_products(
    *,
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    search_query = SearchQuery(
        query,
        config="russian"
    )

    search_vector = (
        SearchVector("name", weight="A", config="russian") +
        SearchVector("brand", weight="B", config="russian") +
        SearchVector("category", weight="C", config="russian")
    )

    qs = (
        Product.objects
        .annotate(
            rank=SearchRank(search_vector, search_query)
        )
        .filter(rank__gt=0)
        .order_by("-rank")
    )

    total = qs.count()
    results = qs[offset: offset + limit]

    return results, total

def suggest_products(
    *,
    query: str,
    limit: int = 10,
):

    if len(query) < 3:
        return []

    qs = (
        Product.objects
        .filter(
            name__istartswith=query
        )
        .values_list("name", flat=True)
        .distinct()[:limit]
    )

    return list(qs)