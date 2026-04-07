from src.repositories.premium_adoption_repository import get_by_dimension


def _list_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [{dimension: col[0], "value": col[1]} for col in columns]


def list_by_country():
    return _list_by_dimension("country")


def list_by_age_group():
    return _list_by_dimension("age_group")


def list_by_annual_income_group():
    return _list_by_dimension("annual_income_group")


def list_by_education_level():
    return _list_by_dimension("education_level")


def list_by_device_type():
    return _list_by_dimension("device_type")
