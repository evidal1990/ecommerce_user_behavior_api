from src.repositories.avg_daily_session_time_repository import get_by_dimension


def get_avg_daily_session_time_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {dimension: col[0], "type": col[1], "subtype": "minutes", "value": col[2]}
        for col in columns
    ]
