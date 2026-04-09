from src.repositories.preferred_product_category_repository import get_by_dimension


def get_preferred_product_category_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "product_category": col[2],
            "value": col[3],
        }
        for col in columns
    ]
