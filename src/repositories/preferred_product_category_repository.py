from src.core.database import get_connection
from textwrap import dedent


def get_by_dimension(dimension: str):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = dedent(
            """
            select
                dimensions ->> %s as dimension,
                kpi_type,
                dimension_value,
                SUM(kpi_value) as value
            from
                kpis
            where
                kpi_name = 'preferred_product_category'
                and dimensions ->> %s <> ''
            group by
                dimension_value,
                dimensions ->> %s,
                kpi_type,
                dimension_name
            order by
                dimension_value,
                dimension
            """
        )

        cur.execute(
            query,
            (dimension, dimension, dimension),
        )
        rows = cur.fetchall()
        return rows
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
