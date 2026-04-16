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


def get_users_avg_product_views_per_day():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_product_views_per_day * count_users) / SUM(count_users), 
                0
            ) as avg_product_views_per_day
        from
            aggregations
        """
    )
    return _fetch_all(query)

def get_users_avg_brand_loyalty_score():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_brand_loyalty_score * count_users) / SUM(count_users), 
                0
            ) as avg_brand_loyalty_score
        from
            aggregations
        """
    )
    return _fetch_all(query)

def get_users_avg_cart_abandonment_rate():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_cart_abandonment_rate * count_users) / SUM(count_users), 
                0
            ) as avg_cart_abandonment_rate
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_avg_daily_session_time():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_daily_session_time_minutes * count_users) / SUM(count_users), 
                0
            ) as avg_daily_session_time
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_avg_purchase_conversion_rate():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_purchase_conversion_rate * count_users) / SUM(count_users), 
                0
            ) as avg_purchase_conversion_rate
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_avg_coupon_usage_frequency():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_coupon_usage_frequency * count_users) / SUM(count_users), 
                0
            ) as avg_coupon_usage
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_has_children_group():
    query = dedent(
        """
        select
            has_children_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            has_children_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_country():
    query = dedent(
        """
        select
            country,
            COUNT(id) as total_users
        from
            aggregations
        group by
            country
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_premium_subscription_group():
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


def get_users_grouped_by_education_level():
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


def get_users_grouped_by_gender():
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


def get_users_grouped_by_neighborhood():
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


def get_users_grouped_by_device_type():
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


def get_users_grouped_by_age_group():
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


def get_users_grouped_by_annual_income_group():
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
