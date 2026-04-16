from src.repositories.user_repository import (
    get_total_users as repo_get_total_users,
    get_users_by_annual_income_group as repo_get_users_by_annual_income_group,
    get_users_by_age_group as repo_get_users_by_age_group,
    get_users_by_device_type as repo_get_users_by_device_type,
    get_users_by_neighborhood as repo_get_users_by_neighborhood,
    get_users_by_gender as repo_get_users_by_gender,
    get_users_by_education_level as repo_get_users_by_education_level,
    get_users_by_premium_subscription_group as repo_get_users_by_premium_subscription_group,
    get_users_by_country as repo_get_users_by_country,
)

_REPO_BY_DIMENSION = {
    "country": repo_get_users_by_country,
    "premium_subscription_group": repo_get_users_by_premium_subscription_group,
    "education_level": repo_get_users_by_education_level,
    "gender": repo_get_users_by_gender,
    "neighborhood": repo_get_users_by_neighborhood,
    "device_type": repo_get_users_by_device_type,
    "age_group": repo_get_users_by_age_group,
    "annual_income_group": repo_get_users_by_annual_income_group,
}


def _rows_to_grouped_items(field_key: str, rows: list[tuple]) -> list[dict]:
    return [{field_key: row[0], "total_users": int(row[1])} for row in rows]


def users_by_dimension(dimension: str):
    fn = _REPO_BY_DIMENSION.get(dimension)
    if fn is None:
        raise ValueError(f"Invalid dimension: {dimension}")
    return _rows_to_grouped_items(dimension, fn())


def users_by_premium_subscription_group():
    return users_by_dimension("premium_subscription_group")


def users_by_education_level():
    return users_by_dimension("education_level")


def users_by_gender():
    return users_by_dimension("gender")


def users_by_neighborhood():
    return users_by_dimension("neighborhood")


def users_by_device_type():
    return users_by_dimension("device_type")


def users_by_age_group():
    return users_by_dimension("age_group")


def users_by_annual_income_group():
    return users_by_dimension("annual_income_group")


def total_users():
    rows = repo_get_total_users()
    return {"total_users": int(rows[0][0])}
