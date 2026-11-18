from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool

from core.config import settings

pool: ThreadedConnectionPool | None = None


def init_pool() -> None:
    global pool
    pool = ThreadedConnectionPool(
        minconn=settings.DB_POOL_MIN,
        maxconn=settings.DB_POOL_MAX,
        cursor_factory=RealDictCursor,
        **settings.db_params,
    )


def close_pool() -> None:
    if pool:
        pool.closeall()


def get_db():
    conn = pool.getconn()
    cur = conn.cursor()
    try:
        yield cur
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        pool.putconn(conn)
