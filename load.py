from sqlalchemy import create_engine
import os
import pandas as pd

DB_URL = os.environ.get("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/etl_demo")
engine = create_engine(DB_URL, future=True)

def upsert_orders(df: pd.DataFrame, table_name="orders"):
    # MVP: append. For production use COPY or ON CONFLICT upsert.
    df.to_sql(table_name, engine, if_exists="append", index=False, method='multi', chunksize=1000)

if __name__ == "__main__":
    import transform, extract
    raw = extract.extract_csv("../raw_data/orders.csv")
    df = transform.transform(raw)
    upsert_orders(df)
    print("Loaded rows:", len(df))