from src.services.base_service import grouped_dicts_to_dimension_value
from src.repositories import (
    repo_get_users_grouped_by_country,
    repo_get_users_grouped_by_premium_subscription_group,
    repo_get_users_grouped_by_education_level,
    repo_get_users_grouped_by_gender,
    repo_get_users_grouped_by_neighborhood,
    repo_get_users_grouped_by_device_type,
    repo_get_users_grouped_by_age_group,
    repo_get_users_grouped_by_annual_income_group,
    repo_get_users_grouped_by_has_children_group,
    repo_get_users_grouped_by_preferred_payment_method,
    repo_get_users_grouped_by_preferred_payment_method_and_country,
    repo_get_users_grouped_by_preferred_payment_method_and_age_group,
    repo_get_users_grouped_by_preferred_payment_method_and_annual_income_group,
    repo_get_users_grouped_by_product_category_preference,
    repo_get_users_grouped_by_product_category_preference_and_country,
    repo_get_users_grouped_by_product_category_preference_and_age_group,
    repo_get_users_grouped_by_product_category_preference_and_annual_income_group,
    repo_get_users_grouped_by_household_size_group,
    repo_get_users_grouped_by_brand_loyalty_score_group,
    repo_get_users_grouped_by_impulse_buying_score_group,
    repo_get_users_grouped_by_social_media_influence_score_group,
    repo_get_users_grouped_by_stress_from_financial_decisions_level_group,
    repo_get_users_grouped_by_referral_count_group,
    repo_get_users_grouped_by_impulse_buying_score_group,
    repo_get_users_grouped_by_browse_to_buy_ratio_group,
    repo_get_users_grouped_by_return_rate_group,
    repo_get_users_grouped_by_purchase_conversion_rate_group,
    repo_get_users_grouped_by_social_sharing_frequency_group,
    repo_get_users_grouped_by_cart_abandonment_rate_group,
    repo_get_users_grouped_by_premium_subscription_group_and_country,
    repo_get_users_grouped_by_premium_subscription_group_and_age_group,
    repo_get_users_grouped_by_premium_subscription_group_and_annual_income_group,
)

_REPO_BY_DIMENSION = {
    "country": repo_get_users_grouped_by_country,
    "premium_subscription": repo_get_users_grouped_by_premium_subscription_group,
    "education_level": repo_get_users_grouped_by_education_level,
    "gender": repo_get_users_grouped_by_gender,
    "neighborhood": repo_get_users_grouped_by_neighborhood,
    "device_type": repo_get_users_grouped_by_device_type,
    "age_group": repo_get_users_grouped_by_age_group,
    "annual_income": repo_get_users_grouped_by_annual_income_group,
    "has_children": repo_get_users_grouped_by_has_children_group,
    "household_size": repo_get_users_grouped_by_household_size_group,
    "brand_loyalty_score": repo_get_users_grouped_by_brand_loyalty_score_group,
    "impulse_buying_score": repo_get_users_grouped_by_impulse_buying_score_group,
    "social_media_influence_score": repo_get_users_grouped_by_social_media_influence_score_group,
    "stress_from_financial_decisions_level": repo_get_users_grouped_by_stress_from_financial_decisions_level_group,
    "referral_count": repo_get_users_grouped_by_referral_count_group,
    "impulse_buying_score": repo_get_users_grouped_by_impulse_buying_score_group,
    "browse_to_buy_ratio": repo_get_users_grouped_by_browse_to_buy_ratio_group,
    "return_rate": repo_get_users_grouped_by_return_rate_group,
    "purchase_conversion_rate": repo_get_users_grouped_by_purchase_conversion_rate_group,
    "social_sharing_frequency": repo_get_users_grouped_by_social_sharing_frequency_group,
    "cart_abandonment_rate": repo_get_users_grouped_by_cart_abandonment_rate_group,
    "premium_adoption": repo_get_users_grouped_by_premium_subscription_group,
    "premium_adoption_by_country": repo_get_users_grouped_by_premium_subscription_group_and_country,
    "premium_adoption_by_age_group": repo_get_users_grouped_by_premium_subscription_group_and_age_group,
    "premium_adoption_by_annual_income": repo_get_users_grouped_by_premium_subscription_group_and_annual_income_group,
    "preferred_payment_method": repo_get_users_grouped_by_preferred_payment_method,
    "preferred_payment_method_by_country": repo_get_users_grouped_by_preferred_payment_method_and_country,
    "preferred_payment_method_by_age_group": repo_get_users_grouped_by_preferred_payment_method_and_age_group,
    "preferred_payment_method_by_annual_income": repo_get_users_grouped_by_preferred_payment_method_and_annual_income_group,
    "product_category_preference": repo_get_users_grouped_by_product_category_preference,
    "product_category_preference_by_country": repo_get_users_grouped_by_product_category_preference_and_country,
    "product_category_preference_by_age_group": repo_get_users_grouped_by_product_category_preference_and_age_group,
    "product_category_preference_by_annual_income": repo_get_users_grouped_by_product_category_preference_and_annual_income_group,
}

_MULTI_DIMENSION_FIELD_NAMES: dict[str, list[str]] = {
    "premium_adoption_by_country": [
        "country",
        "premium_adoption",
    ],
    "premium_adoption_by_age_group": [
        "age_group",
        "premium_adoption",
    ],
    "premium_adoption_by_annual_income": [
        "annual_income_group",
        "premium_adoption",
    ],
    "preferred_payment_method_by_country": [
        "country",
        "preferred_payment_method",
    ],
    "preferred_payment_method_by_age_group": [
        "age_group",
        "preferred_payment_method",
    ],
    "preferred_payment_method_by_annual_income": [
        "annual_income_group",
        "preferred_payment_method",
    ],
    "product_category_preference_by_country": [
        "country",
        "product_category_preference",
    ],
    "product_category_preference_by_age_group": [
        "age_group",
        "product_category_preference",
    ],
    "product_category_preference_by_annual_income": [
        "annual_income_group",
        "product_category_preference",
    ],
}


def _dimension_field_names(group_by: str, dimension_count: int) -> list[str]:
    if dimension_count < 1:
        raise ValueError("expected at least one dimension column before the metric")
    if dimension_count == 1:
        return [group_by]
    names = _MULTI_DIMENSION_FIELD_NAMES.get(group_by)
    if names is None or len(names) != dimension_count:
        raise ValueError(
            f"Add _MULTI_DIMENSION_FIELD_NAMES[{group_by!r}] with "
            f"{dimension_count} name(s) in the same order as the SELECT dimensions."
        )
    return names


def _rows_to_grouped_items(
    field_key: str,
    rows: list[tuple],
):
    if not rows:
        return []
    width = len(rows[0])
    dim_count = width - 1
    field_names = _dimension_field_names(field_key, dim_count)
    result = []
    for row in rows:
        if len(row) != width:
            raise ValueError("all rows must have the same number of columns")
        item = {field_names[i]: row[i] for i in range(dim_count)}
        item["total_users"] = float(row[-1])
        result.append(item)
    return result


def users_analytics(
    group_by: str | None = None,
):
    fn = _REPO_BY_DIMENSION.get(group_by)
    if fn is None:
        raise ValueError(f"Invalid dimension: {group_by}")

    rows = fn()
    items = _rows_to_grouped_items(group_by, rows)
    return grouped_dicts_to_dimension_value(items, value_key="total_users")
