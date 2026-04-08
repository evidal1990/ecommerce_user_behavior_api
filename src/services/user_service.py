from src.repositories.user_repository import get_by_dimension


def _list_by_dimension(kpi_name: str):
    columns = get_by_dimension(kpi_name)
    return [{kpi_name: col[0], "type": col[1], "value": col[2]} for col in columns]


def list_by_employment_status():
    return _list_by_dimension("users_by_employment_status")


def list_by_annual_income_group():
    return _list_by_dimension("users_by_annual_income")


def list_by_age_group():
    return _list_by_dimension("users_by_age_group")


def list_by_device_type():
    return _list_by_dimension("users_by_device_type")


def list_by_neighborhood():
    return _list_by_dimension("users_by_urban_rural")


def list_by_education_level():
    return _list_by_dimension("users_by_education_level")


def list_by_gender():
    return _list_by_dimension("users_by_gender")


def list_by_country():
    return _list_by_dimension("users_by_country")


def list_by_has_children():
    return _list_by_dimension("users_by_has_children")
