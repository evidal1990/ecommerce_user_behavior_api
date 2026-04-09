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
                dimension_value,
                kpi_type,
                kpi_value
            from
                kpis
            where
                kpi_name = 'daily_active_users'
                and dimension_name = %s  
            order by
                dimension_value
            """
        )

        cur.execute(query, (dimension,))
        rows = cur.fetchall()
        return rows
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
