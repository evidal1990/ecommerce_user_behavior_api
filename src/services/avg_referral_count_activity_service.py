from src.repositories.avg_referral_count_activity_repository import get_by_dimension


def get_avg_referral_count_activity_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [
        {
            dimension: col[0],
            "type": col[1],
            "subtype": "referrals",
            "value": col[2],
        }
        for col in columns
    ]
