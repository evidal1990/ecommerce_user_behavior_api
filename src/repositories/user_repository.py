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
