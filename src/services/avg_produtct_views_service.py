from src.repositories.avg_product_views_repository import get_by_dimension


def get_avg_product_views_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {dimension: col[0], "type": col[1], "subtype": "products_viewed", "value": col[2]}
        for col in columns
    ]
