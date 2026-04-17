from src.repositories import (
    repo_get_total_users,
    repo_get_users_avg_coupon_usage_frequency,
    repo_get_users_avg_purchase_conversion_rate,
    repo_get_users_avg_daily_session_time,
    repo_get_users_avg_cart_abandonment_rate,
    repo_get_users_avg_brand_loyalty_score,
    repo_get_users_avg_product_views_per_day,
    repo_get_users_avg_app_usage_frequency,
    repo_get_users_avg_referral_count,
    repo_get_users_churn_rate,
    repo_get_users_nps,
)

_REPO_BY_METRIC = {
    "avg_coupon_usage_per_user": repo_get_users_avg_coupon_usage_frequency,
    "avg_purchase_conversion_rate": repo_get_users_avg_purchase_conversion_rate,
    "avg_daily_session_time": repo_get_users_avg_daily_session_time,
    "avg_cart_abandonment_rate": repo_get_users_avg_cart_abandonment_rate,
    "avg_brand_loyalty_score": repo_get_users_avg_brand_loyalty_score,
    "avg_product_views_per_day": repo_get_users_avg_product_views_per_day,
    "avg_app_usage_frequency": repo_get_users_avg_app_usage_frequency,
    "avg_referral_count": repo_get_users_avg_referral_count,
    "churn_rate": repo_get_users_churn_rate,
    "net_promoter_score": repo_get_users_nps,
    "total_users": repo_get_total_users,
}


def _metric_field_names(metric: str, dimension_count: int) -> list[str]:
    if dimension_count < 1:
        raise ValueError("expected at least one metric column before the dimension")
    if dimension_count == 1:
        return [metric]
    return [metric]


def _rows_to_grouped_items(
    field_key: str,
    rows: list[tuple],
    metric: str,
):
    if not rows:
        return []
    width = len(rows[0])
    if width == 1:
        return [{metric: float(rows[0][0])}]
    dim_count = width - 1
    field_names = _metric_field_names(field_key, dim_count)
    result = []
    for row in rows:
        if len(row) != width:
            raise ValueError("all rows must have the same number of columns")
        item = {field_names[i]: row[i] for i in range(dim_count)}
        item[metric] = float(row[-1])
        result.append(item)
    return result


def metrics_analytics(
    group_by: str | None = None,
    metric: str = "total_users",
):
    fn = _REPO_BY_METRIC.get(metric)
    if fn is None:
        raise ValueError(f"Invalid metric: {metric}")

    rows = fn()
    return _rows_to_grouped_items(
        group_by,
        rows,
        metric,
    )
