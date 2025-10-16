import pandas as pd

def transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset=["order_id"])
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
    df['item_price'] = pd.to_numeric(df['item_price'], errors='coerce').fillna(0)
    df['qty'] = pd.to_numeric(df['qty'], errors='coerce').fillna(0).astype(int)
    df['total_price'] = df['item_price'] * df['qty']
    df = df[df['order_date'].notna()]
    for c in df.select_dtypes(include=['object']).columns:
        df[c] = df[c].str.strip()
    return df

if __name__ == "__main__":
    import extract
    raw = extract.extract_csv("../raw_data/orders.csv")
    clean = transform(raw)
    print("Rows after transform:", len(clean))