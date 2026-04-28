from src.extract import load_processed_data
from src.transform import transform_data
from src.load import load_raw_tables


def run_pipeline():
    print("Starting ETL pipeline...")

    # 1. Extract processed CSV files
    clients, health_products, health_lapses = load_processed_data()

    print("Extract complete.")
    print(f"Clients rows: {len(clients)}")
    print(f"Products rows: {len(health_products)}")
    print(f"Lapses rows: {len(health_lapses)}")

    # 2. Transform data
    clients_clean, health_products_clean, health_lapses_clean = transform_data(
        clients,
        health_products,
        health_lapses
    )

    print("Transform complete.")

    # 3. Load into PostgreSQL staging tables
    load_raw_tables(
        clients_clean,
        health_lapses_clean,
        health_products_clean
    )

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()