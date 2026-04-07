from src.repositories.premium_adoption_repository import get_by_dimension


def list_by_country():
    columns = get_by_dimension("country")

    return [{"country": col[0], "value": col[1]} for col in columns]


def list_by_age_group():
    columns = get_by_dimension("age_group")

    return [{"age_group": col[0], "value": col[1]} for col in columns]


def list_by_annual_income_group():
    columns = get_by_dimension("annual_income_group")

    return [{"annual_income": col[0], "value": col[1]} for col in columns]


def list_by_education_level():
    columns = get_by_dimension("education_level")

    return [{"education_level": col[0], "value": col[1]} for col in columns]


def list_by_device_type():
    columns = get_by_dimension("device_type")

    return [{"device_type": col[0], "value": col[1]} for col in columns]
