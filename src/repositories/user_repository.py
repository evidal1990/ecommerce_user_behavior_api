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


def get_users_grouped_by_household_size_group():
    query = dedent(
        """
        select
            household_size_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            household_size_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_impulse_buying_score_group():
    query = dedent(
        """
        select
            brand_loyalty_score_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            brand_loyalty_score_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_brand_loyalty_score_group():
    query = dedent(
        """
        select
            impulse_buying_score_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            impulse_buying_score_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_social_media_influence_score_group():
    query = dedent(
        """
        select
            social_media_influence_score_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            social_media_influence_score_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_stress_from_financial_decisions_level_group():
    query = dedent(
        """
        select
            stress_from_financial_decisions_level_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            stress_from_financial_decisions_level_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_referral_count_group():
    query = dedent(
        """
        select
            referral_count_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            referral_count_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_impulse_buying_score_group():
    query = dedent(
        """
        select
            impulse_buying_score_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            impulse_buying_score_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_browse_to_buy_ratio_group():
    query = dedent(
        """
        select
            browse_to_buy_ratio_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            browse_to_buy_ratio_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_return_rate_group():
    query = dedent(
        """
        select
            return_rate_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            return_rate_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_purchase_conversion_rate_group():
    query = dedent(
        """
        select
            purchase_conversion_rate_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            purchase_conversion_rate_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_social_sharing_frequency_group():
    query = dedent(
        """
        select
            social_sharing_frequency_per_year_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            social_sharing_frequency_per_year_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_cart_abandonment_rate_group():
    query = dedent(
        """
        select
            cart_abandonment_rate_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            cart_abandonment_rate_group
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


def get_users_grouped_by_premium_subscription_group_and_country():
    query = dedent(
        """
        select
            country,
            premium_subscription_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            country,
            premium_subscription_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_premium_subscription_group_and_age_group():
    query = dedent(
        """
        select
            age_group,
            premium_subscription_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            age_group,
            premium_subscription_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_premium_subscription_group_and_annual_income_group():
    query = dedent(
        """
        select
            annual_income_group,
            premium_subscription_group,
            COUNT(id) as total_users
        from
            aggregations
        group by
            annual_income_group,
            premium_subscription_group
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_preferred_payment_method():
    query = dedent(
        """
        select
            preferred_payment_method,
            COUNT(id) as total_users
        from
            aggregations
        group by
            preferred_payment_method
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_preferred_payment_method_and_country():
    query = dedent(
        """
        select
            country,
            preferred_payment_method,
            COUNT(id) as total_users
        from
            aggregations
        group by
            country,
            preferred_payment_method
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_preferred_payment_method_and_age_group():
    query = dedent(
        """
        select
            age_group,
            preferred_payment_method,
            COUNT(id) as total_users
        from
            aggregations
        group by
            age_group,
            preferred_payment_method
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_preferred_payment_method_and_annual_income_group():
    query = dedent(
        """
        select
            annual_income_group,
            preferred_payment_method,
            COUNT(id) as total_users
        from
            aggregations
        group by
            annual_income_group,
            preferred_payment_method
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_product_category_preference():
    query = dedent(
        """
        select
            product_category_preference,
            COUNT(id) as total_users
        from
            aggregations
        group by
            product_category_preference
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_product_category_preference_and_country():
    query = dedent(
        """
        select
            country,
            product_category_preference,
            COUNT(id) as total_users
        from
            aggregations
        group by
            country,
            product_category_preference
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_product_category_preference_and_age_group():
    query = dedent(
        """
        select
            age_group,
            product_category_preference,
            COUNT(id) as total_users
        from
            aggregations
        group by
            age_group,
            product_category_preference
        """
    )
    return _fetch_all(query)


def get_users_grouped_by_product_category_preference_and_annual_income_group():
    query = dedent(
        """
        select
            annual_income_group,
            product_category_preference,
            COUNT(id) as total_users
        from
            aggregations
        group by
            annual_income_group,
            product_category_preference
        """
    )
    return _fetch_all(query)


def get_top_countries():
    query = dedent(
        """
        select
            country,
            COUNT(id) as total_users
        from
            aggregations
        group by
            country
        order by
            total_users desc
        """
    )
    return _fetch_all(query)[:3]


def get_top_product_categories():
    query = dedent(
        """
        select
            product_category_preference,
            COUNT(id) as total_users
        from
            aggregations
        group by
            product_category_preference
        order by
            total_users desc
        """
    )
    return _fetch_all(query)[:3]
