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
                dimensions ->>%s as dimension,
                kpi_type,
                SUM(kpi_value) as value
            from
                kpis
            where
                kpi_name = 'net_promoter_score'
                and dimensions ->>%s is not null
                and dimensions ->>%s <> ''
            group by
                dimensions ->>%s,
                kpi_type
            order by
                value desc
            """
        )

        cur.execute(
            query,
            (
                dimension,
                dimension,
                dimension,
                dimension,
            ),
        )
        rows = cur.fetchall()
        return rows
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
