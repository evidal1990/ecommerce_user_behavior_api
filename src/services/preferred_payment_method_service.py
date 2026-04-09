from src.repositories.preferred_payment_method_repository import get_by_dimension


def get_preferred_payment_method_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "payment_method": col[2],
            "dimension_value": col[3],
        }
        for col in columns
    ]
