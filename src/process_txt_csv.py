from pathlib import Path
import pandas as pd


RAW_FILE = Path("C:/Users/tvila/OneDrive/Documents/Alignd_Data_Pipeline/data/raw/health_products.txt")
OUTPUT_FILE = Path("C:/Users/tvila/OneDrive/Documents/Alignd_Data_Pipeline/data/processed/health_products_clean.csv")


COLUMN_NAMES = [
    "product_id",
    "product_name",
    "tier_level",
    "status"
]


def process_txt_to_csv():
    print("Starting TXT to CSV process...")

    df = pd.read_csv(
        RAW_FILE,
        sep="|",
        skiprows=1,        
        header=None,       
        names=COLUMN_NAMES,
        dtype=str,
        encoding="utf-8",
        engine="python",
        on_bad_lines="skip"
    )

    
    df = df.dropna(how="all")

    for col in df.columns:
        df[col] = df[col].str.strip()

    
    df["product_id"] = df["product_id"].str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")

    print("SUCCESS")
    print(f"Saved to: {OUTPUT_FILE}")
    print(f"Rows processed: {len(df)}")
    print(f"Columns: {list(df.columns)}")
    print(df.head())


if __name__ == "__main__":
    process_txt_to_csv()