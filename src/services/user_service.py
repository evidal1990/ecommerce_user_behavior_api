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
    "avg_coupon_usage_frequency": repo_get_users_avg_coupon_usage_frequency,
}

_REPO_BY_METRIC = {
    "total_users": repo_get_total_users,
    "avg_coupon_usage_per_user": repo_get_users_avg_coupon_usage_frequency,
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
