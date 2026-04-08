from src.repositories.avg_coupon_usage_frequency_repository import get_by_dimension


def get_avg_coupon_usage_frequency_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {dimension: col[0], "type": col[1], "subtype": "days", "value": col[2]}
        for col in columns
    ]
