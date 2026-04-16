from src.repositories import (
    repo_get_total_users,
    repo_get_users_grouped_by_country,
    repo_get_users_grouped_by_premium_subscription_group,
    repo_get_users_grouped_by_education_level,
    repo_get_users_grouped_by_gender,
    repo_get_users_grouped_by_neighborhood,
    repo_get_users_grouped_by_device_type,
    repo_get_users_grouped_by_age_group,
    repo_get_users_grouped_by_annual_income_group,
    repo_get_users_grouped_by_has_children_group,
    repo_get_users_avg_coupon_usage_frequency,
    repo_get_users_avg_purchase_conversion_rate,
    repo_get_users_avg_daily_session_time,
    repo_get_users_avg_cart_abandonment_rate,
    repo_get_users_avg_brand_loyalty_score,
    repo_get_users_avg_product_views_per_day,
    repo_get_users_avg_app_usage_frequency,
    repo_get_users_avg_referral_count,
    repo_get_users_grouped_by_household_size_group,
    repo_get_users_grouped_by_brand_loyalty_score_group,
    repo_get_users_grouped_by_impulse_buying_score_group,
    repo_get_users_grouped_by_social_media_influence_score_group,
    repo_get_users_grouped_by_stress_from_financial_decisions_level_group,
)

_REPO_BY_DIMENSION = {
    "country": repo_get_users_grouped_by_country,
    "premium_subscription_group": repo_get_users_grouped_by_premium_subscription_group,
    "education_level": repo_get_users_grouped_by_education_level,
    "gender": repo_get_users_grouped_by_gender,
    "neighborhood": repo_get_users_grouped_by_neighborhood,
    "device_type": repo_get_users_grouped_by_device_type,
    "age_group": repo_get_users_grouped_by_age_group,
    "annual_income_group": repo_get_users_grouped_by_annual_income_group,
    "has_children_group": repo_get_users_grouped_by_has_children_group,
    "household_size_group": repo_get_users_grouped_by_household_size_group,
    "brand_loyalty_score_group": repo_get_users_grouped_by_brand_loyalty_score_group,
    "impulse_buying_score_group": repo_get_users_grouped_by_impulse_buying_score_group,
    "social_media_influence_score_group": repo_get_users_grouped_by_social_media_influence_score_group,
    "stress_from_financial_decisions_level_group": repo_get_users_grouped_by_stress_from_financial_decisions_level_group,
}

_REPO_BY_METRIC = {
    "total_users": repo_get_total_users,
    "avg_coupon_usage_per_user": repo_get_users_avg_coupon_usage_frequency,
    "avg_purchase_conversion_rate": repo_get_users_avg_purchase_conversion_rate,
    "avg_daily_session_time": repo_get_users_avg_daily_session_time,
    "avg_cart_abandonment_rate": repo_get_users_avg_cart_abandonment_rate,
    "avg_brand_loyalty_score": repo_get_users_avg_brand_loyalty_score,
    "avg_product_views_per_day": repo_get_users_avg_product_views_per_day,
    "avg_app_usage_frequency": repo_get_users_avg_app_usage_frequency,
    "avg_referral_count": repo_get_users_avg_referral_count,
}


def _rows_to_grouped_items(
    field_key: str,
    rows: list[tuple],
    metric: str,
):
    return [
        {
            field_key: row[0],
            metric: float(row[1]),
        }
        for row in rows
    ]


def users_analytics(
    group_by: str | None = None,
    metric: str = "total_users",
):
    if group_by:
        fn = _REPO_BY_DIMENSION.get(group_by)
        if fn is None:
            raise ValueError(f"Invalid dimension: {group_by}")

        rows = fn()
        return _rows_to_grouped_items(
            group_by,
            rows,
            metric,
        )

    fn = _REPO_BY_METRIC.get(metric)
    if fn is None:
        raise ValueError(f"Invalid metric: {metric}")

    rows = fn()
    return {
        "metric": metric,
        "value": float(
            rows[0][0],
        ),
    }
