from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
PROCESSED_DIR = BASE_DIR / "data/processed"


def load_processed_data():
    print("Loading processed CSV files...")

    clients = pd.read_csv(PROCESSED_DIR / "clients.csv")
    health_products = pd.read_csv(PROCESSED_DIR / "health_products_clean.csv")
    health_lapses = pd.read_csv(PROCESSED_DIR / "health_lapses.csv")

    print("Data loaded successfully.")

    return clients, health_products, health_lapses