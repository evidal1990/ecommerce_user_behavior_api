from src.repositories.user_repository import (
    get_total_users as repo_get_total_users,
    get_users_by_annual_income_group as repo_get_users_by_annual_income_group,
)


def users_by_annual_income_group():
    columns = repo_get_users_by_annual_income_group()
    return [{"annual_income_group": col[0], "total_users": col[1]} for col in columns]


def total_users():
    rows = repo_get_total_users()
    return {"total_users": rows[0][0]}
