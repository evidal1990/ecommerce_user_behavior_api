from src.repositories.user_repository import (
    get_total_users as repo_get_total_users,
    get_users_by_annual_income_group as repo_get_users_by_annual_income_group,
    get_users_by_age_group as repo_get_users_by_age_group,
    get_users_by_device_type as repo_get_users_by_device_type,
    get_users_by_neighborhood as repo_get_users_by_neighborhood,
)


def users_by_neighborhood():
    columns = repo_get_users_by_neighborhood()
    return [
        {
            "neighborhood": col[0],
            "total_users": col[1],
        }
        for col in columns
    ]


def users_by_device_type():
    columns = repo_get_users_by_device_type()
    return [
        {
            "device_type": col[0],
            "total_users": col[1],
        }
        for col in columns
    ]


def users_by_age_group():
    columns = repo_get_users_by_age_group()
    return [
        {
            "age_group": col[0],
            "total_users": col[1],
        }
        for col in columns
    ]


def users_by_annual_income_group():
    columns = repo_get_users_by_annual_income_group()
    return [
        {
            "annual_income_group": col[0],
            "total_users": col[1],
        }
        for col in columns
    ]


def total_users():
    rows = repo_get_total_users()
    return {"total_users": rows[0][0]}
