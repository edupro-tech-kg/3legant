from .models import Product


def get_active_products():
    return Product.objects.filter(is_active=True)

def get_products_by_category(category_id):
    return Product.objects.filter(
        is_active=True,
        category_id=category_id
    )

def get_product_by_id(product_id):
    return Product.objects.filter(
        id=product_id,
        is_active=True
    ).first()

def get_products_by_brand(brand_id):
    return Product.objects.filter(
        is_active=True,
        brand_id=brand_id
    )