from src.repositories.avg_purchase_conversion_rate_respository import get_by_dimension


def get_avg_purcaase_conversion_rate_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "subtype": "conversion_rate",
            "value": col[2],
        }
        for col in columns
    ]
