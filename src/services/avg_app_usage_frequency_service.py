from src.repositories.avg_app_usage_frequency_repository import get_by_dimension


def _list_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {dimension: col[0], "type": col[1], "frequency": "days", "value": col[2]}
        for col in columns
    ]


def list_by_country():
    return _list_by_dimension("country")


def list_by_age_group():
    return _list_by_dimension("age_group")


def list_by_device_type():
    return _list_by_dimension("device_type")
