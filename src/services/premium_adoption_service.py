from src.repositories.premium_adoption_repository import get_by_dimension

ALLOWED_DIMENSIONS = {
    "country",
}


def list(dimension: str):
    if dimension not in ALLOWED_DIMENSIONS:
        raise ValueError("Invalid dimension")
    columns = get_by_dimension(dimension)

    return [{"country": col[0], "value": col[1]} for col in columns]


def list_by_country():
    return list("country")
