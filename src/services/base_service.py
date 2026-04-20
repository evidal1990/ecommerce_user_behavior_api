from decimal import Decimal
from typing import Any


def _jsonable_number(value: Any) -> Any:
    if isinstance(value, Decimal):
        return float(value)
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        return float(value)
    return value


def grouped_dicts_to_dimension_value(
    items: list[dict[str, Any]],
    value_key: str,
) -> list[dict[str, Any]]:
    """
    Converte o retorno de _rows_to_grouped_items para
    [{"dimension": ..., "value": ...}].

    - Só a métrica (ex.: total_users): dimension = nome da métrica (value_key).
    - Uma dimensão + métrica: dimension = valor da dimensão (escalar).
    - Várias dimensões + métrica: dimension = dict {campo: valor, ...}.
    """
    out: list[dict[str, Any]] = []
    for item in items:
        if value_key not in item:
            raise ValueError(f"expected {value_key!r} in row {item!r}")
        dim_keys = [k for k in item if k != value_key]
        val = _jsonable_number(item[value_key])
        if not dim_keys:
            out.append({"dimension": value_key, "value": val})
        elif len(dim_keys) == 1:
            out.append({"dimension": item[dim_keys[0]], "value": val})
        else:
            out.append(
                {
                    "dimension": {k: item[k] for k in dim_keys},
                    "value": val,
                }
            )
    return out
