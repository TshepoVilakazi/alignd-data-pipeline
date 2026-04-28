from src.config import engine
from sqlalchemy import text


def create_schemas():
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS staging;"))
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS warehouse;"))


def load_table(df, table_name, schema="staging"):
    df.to_sql(
        name=table_name,
        con=engine,
        schema=schema,
        if_exists="replace",
        index=False
    )

    print(f"Loaded {schema}.{table_name}")


def load_raw_tables(clients, health_lapses, health_products):
    create_schemas()

    load_table(clients, "stg_clients")
    load_table(health_lapses, "stg_health_lapses")
    load_table(health_products, "stg_health_products")

    print("All staging tables loaded successfully.")