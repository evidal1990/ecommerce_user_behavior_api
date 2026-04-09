from src.repositories.churn_rate_repository import get_by_dimension


def get_churn_rate_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "subtype": col[2],
            "date": col[3],
            "value": col[4],
        }
        for col in columns
    ]
