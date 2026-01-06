from django.db.models import Q
from products.models import Product


def search_products(
    *,
    query: str,
    limit: int = 20,
    offset: int = 0,
):
    """
    Search products by title, brand, and category.
    Works with SQLite using Django ORM.
    """
    search_terms = query.split()
    
    # Build Q objects for searching
    q_objects = Q()
    for term in search_terms:
        q_objects |= (
            Q(title__icontains=term) |
            Q(brand__title__icontains=term) |
            Q(category__title__icontains=term) |
            Q(description__icontains=term)
        )

    qs = (
        Product.objects
        .filter(q_objects)
        .select_related('brand', 'category')
        .distinct()
        .order_by("-created_at")
    )

    total = qs.count()
    results = qs[offset: offset + limit]

    return results, total


def suggest_products(
    *,
    query: str,
    limit: int = 10,
):
    """
    Suggest product names based on query.
    """
    if len(query) < 2:
        return []

    qs = (
        Product.objects
        .filter(
            title__istartswith=query
        )
        .values_list("title", flat=True)
        .distinct()[:limit]
    )

    return list(qs)