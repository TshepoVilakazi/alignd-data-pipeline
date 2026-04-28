from load import execute_sql


def create_warehouse_tables():
    sql = """
    DROP TABLE IF EXISTS warehouse.fact_lapses;
    DROP TABLE IF EXISTS warehouse.dim_products;
    DROP TABLE IF EXISTS warehouse.dim_clients;

    CREATE TABLE warehouse.dim_clients AS
    SELECT DISTINCT
        client_id,
        income
    FROM staging.stg_clients
    WHERE client_id IS NOT NULL;

    CREATE TABLE warehouse.dim_products AS
    SELECT DISTINCT
        prod_001,
        hospital_plan,
        
    FROM staging.stg_services_products
    WHERE product_id IS NOT NULL;

    CREATE TABLE warehouse.fact_lapses AS
    SELECT
        l.client_id,
        l.product_id,
        l.lapse_date
    FROM staging.stg_services_lapses l
    WHERE l.client_id IS NOT NULL
      AND l.product_id IS NOT NULL;
    """

    execute_sql(sql)
    print("Warehouse tables created successfully.")