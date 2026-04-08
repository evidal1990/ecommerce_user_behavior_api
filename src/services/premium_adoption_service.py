from src.repositories.premium_adoption_repository import get_by_dimension


def get_premium_adoption_by_dimension(dimension: str):
    columns = get_by_dimension(dimension)
    return [{dimension: col[0], "type": col[1], "value": col[2]} for col in columns]
