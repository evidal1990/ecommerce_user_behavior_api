from src.repositories.avg_brand_loyalty_score_repository import get_by_dimension


def get_avg_brand_loyalty_score_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "subtype": "score",
            "value": col[2],
        }
        for col in columns
    ]
