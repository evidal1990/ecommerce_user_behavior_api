from src.repositories.user_repository import (
    get_total_users as repo_get_total_users,
    get_users_grouped_by_annual_income_group as repo_get_users_grouped_by_annual_income_group,
    get_users_grouped_by_age_group as repo_get_users_grouped_by_age_group,
    get_users_grouped_by_device_type as repo_get_users_grouped_by_device_type,
    get_users_grouped_by_neighborhood as repo_get_users_grouped_by_neighborhood,
    get_users_grouped_by_gender as repo_get_users_grouped_by_gender,
    get_users_grouped_by_education_level as repo_get_users_grouped_by_education_level,
    get_users_grouped_by_premium_subscription_group as repo_get_users_grouped_by_premium_subscription_group,
    get_users_grouped_by_country as repo_get_users_grouped_by_country,
    get_users_grouped_by_has_children_group as repo_get_users_grouped_by_has_children_group,
    get_users_avg_coupon_usage_frequency as repo_get_users_avg_coupon_usage_frequency,
    get_users_avg_purchase_conversion_rate as repo_get_users_avg_purchase_conversion_rate,
)

__all__ = [
    repo_get_total_users,
    repo_get_users_grouped_by_annual_income_group,
    repo_get_users_grouped_by_age_group,
    repo_get_users_grouped_by_device_type,
    repo_get_users_grouped_by_neighborhood,
    repo_get_users_grouped_by_gender,
    repo_get_users_grouped_by_education_level,
    repo_get_users_grouped_by_premium_subscription_group,
    repo_get_users_grouped_by_country,
    repo_get_users_grouped_by_has_children_group,
    repo_get_users_avg_coupon_usage_frequency,
    repo_get_users_avg_purchase_conversion_rate,
]
