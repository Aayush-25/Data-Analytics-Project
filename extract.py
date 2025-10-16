# src/extract.py
import pandas as pd
from pathlib import Path

def extract_csv(path: str):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"{path} not found")
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = extract_csv("raw_data/orders.csv")
    print("Extracted rows:", len(df))