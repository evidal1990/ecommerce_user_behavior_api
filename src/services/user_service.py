from src.repositories.user_repository import get_by_dimension


def _list_by_dimension(kpi_name: str):
    columns = get_by_dimension(kpi_name)
    return [{kpi_name: col[0], "type": col[1], "value": col[2]} for col in columns]


def list_by_employment_status():
    return _list_by_dimension("users_by_employment_status")


def list_by_annual_income_group():
    return _list_by_dimension("users_by_annual_income")
