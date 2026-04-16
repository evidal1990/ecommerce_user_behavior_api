from textwrap import dedent

from src.core.database import get_connection


def _fetch_all(query: str):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(query)
        return cur.fetchall()
    finally:
        cur.close()
        conn.close()


def get_users_by_premium_subscription_group():
    query = dedent(
        """
        select
            premium_subscription_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            premium_subscription_group
        """
    )
    return _fetch_all(query)


def get_users_by_education_level():
    query = dedent(
        """
        select
            education_level,
            COUNT(id) as total_users
        from
            aggregations
        group by
            education_level
        """
    )
    return _fetch_all(query)


def get_users_by_gender():
    query = dedent(
        """
        select
            gender,
            COUNT(id) as total_users
        from
            aggregations
        group by
            gender
        """
    )
    return _fetch_all(query)


def get_users_by_neighborhood():
    query = dedent(
        """
        select
            urban_rural as neighborhood,
            COUNT(id) as total_users
        from
            aggregations
        group by
            urban_rural
        """
    )
    return _fetch_all(query)


def get_users_by_device_type():
    query = dedent(
        """
        select
            device_type,
            COUNT(id) as total_users
        from
            aggregations
        group by
            device_type
        """
    )
    return _fetch_all(query)


def get_users_by_age_group():
    query = dedent(
        """
        select
            age_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            age_group
        """
    )
    return _fetch_all(query)


def get_users_by_annual_income_group():
    query = dedent(
        """
        select
            annual_income_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            annual_income_group
        """
    )
    return _fetch_all(query)


def get_total_users():
    query = dedent(
        """
        select
            COUNT(id) as total_users
        from
            aggregations
        """
    )
    return _fetch_all(query)
