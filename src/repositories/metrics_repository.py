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


def get_users_avg_referral_count():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_referral_count * count_users) / SUM(count_users), 
                0
            ) as avg_referral_count
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_avg_app_usage_frequency():
    query = dedent(
        """
        select
            ROUND(
                SUM(avg_app_usage_frequency_per_week * count_users) / SUM(count_users), 
                0
            ) as avg_app_usage_frequency
        from
            aggregations
        """
    )
    return _fetch_all(query)


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


def get_users_churn_rate():
    query = dedent(
        """
        select
            ROUND(
                COUNT(*) filter (
                where
                    last_purchase_date < (now() - interval '90 days')
                ) * 1.0 / COUNT(id) * 100,
                0
            ) as churn_rate
        from
            aggregations
        """
    )
    return _fetch_all(query)


def get_users_nps():
    query = dedent(
        """
        select
              ROUND(((
                SUM(
                    case
                        when brand_loyalty_score_group = 'Promoters' then count_users
                        else 0
                    end
                ) - 
                SUM(
                    case
                        when brand_loyalty_score_group = 'Detractors' then count_users
                        else 0
                    end
                )
            ) * 1.0 / SUM(count_users) * 100 + 100) / 2, 0) as nps_0_100
        from
            aggregations
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
