import pandas as pd
from pathlib import Path


PARQUET_FILE = Path("C:/Users/tvila/OneDrive/Documents/Alignd_Data_Pipeline/data/raw/health_lapses.parquet")
CSV_FILE = Path("C:/Users/tvila/OneDrive/Documents/Alignd_Data_Pipeline/data/processed/health_lapses.csv")


def parquet_to_csv():
    try:
        print("Starting Parquet → CSV conversion...")

        if not PARQUET_FILE.exists():
            raise FileNotFoundError(f"File not found: {PARQUET_FILE}")

        df = pd.read_parquet(PARQUET_FILE, engine="pyarrow")

        print(f"Rows loaded: {len(df)}")
        print(f"Columns: {list(df.columns)}")

        
        df = df.drop_duplicates()

        CSV_FILE.parent.mkdir(parents=True, exist_ok=True)

        df.to_csv(CSV_FILE, index=False, encoding="utf-8")

        print("\n SUCCESS")
        print(f"CSV saved at: {CSV_FILE.resolve()}")

    except Exception as e:
        print("\n ERROR")
        print(e)


if __name__ == "__main__":
    parquet_to_csv()