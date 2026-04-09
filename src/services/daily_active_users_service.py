from src.repositories.daily_active_users_repository import get_by_dimension


def get_daily_active_users_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "subtype": "users",
            "value": col[2],
        }
        for col in columns
    ]
