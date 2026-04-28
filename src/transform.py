import pandas as pd


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
        .str.replace(r"[^\w_]", "", regex=True)
    )

    return df


def trim_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()

    return df


def remove_duplicates(df: pd.DataFrame, subset=None) -> pd.DataFrame:
    df = df.copy()

    before = len(df)
    df = df.drop_duplicates(subset=subset)
    after = len(df)

    print(f"Removed duplicates: {before - after}")

    return df

#NULL income values were imputed using the median because income data is often skewed by very high or very low earners. The median is more robust than the mean and reduces the effect of outliers.
def handle_null_income(clients: pd.DataFrame) -> pd.DataFrame:
    clients = clients.copy()

    if "income" in clients.columns:
        clients["income"] = pd.to_numeric(clients["income"], errors="coerce")

        median_income = clients["income"].median()

        clients["income"] = clients["income"].fillna(median_income)

        print(f"NULL income values filled with median: {median_income}")
    else:
        print("Income column not found. Skipping NULL income handling.")

    return clients


def transform_clients(clients: pd.DataFrame) -> pd.DataFrame:
    print("Transforming clients...")

    clients = clean_column_names(clients)
    clients = trim_text_columns(clients)

    if "client_id" in clients.columns:
        clients = remove_duplicates(clients, subset=["client_id"])
    else:
        clients = remove_duplicates(clients)

    clients = handle_null_income(clients)

    return clients


def transform_health_products(health_products: pd.DataFrame) -> pd.DataFrame:
    print("Transforming services products...")

    health_products = clean_column_names(health_products)
    health_products = trim_text_columns(health_products)
    health_products = remove_duplicates(health_products)

    return health_products


def transform_services_lapses(health_lapses: pd.DataFrame) -> pd.DataFrame:
    print("Transforming services lapses...")

    health_lapses = clean_column_names(health_lapses)
    health_lapses = trim_text_columns(health_lapses)
    health_lapses = remove_duplicates(health_lapses)

    return health_lapses


def transform_data(clients, health_products, health_lapses):
    clients_clean = transform_clients(clients)
    health_products_clean = transform_health_products(health_products)
    health_lapses_clean = transform_services_lapses(health_lapses)

    return clients_clean, health_products_clean, health_lapses_clean