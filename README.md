# ETL Demo - etl-demo-<AAYUSH>

## What this is
A minimal end-to-end ETL demo:
- Extract raw CSV files (`raw_data/orders.csv`)
- Transform (clean, dedup, enrich)
- Load into a DB (SQLite by default, Postgres optional)
- Streamlit dashboard to visualize KPIs

## Quick setup (using conda)
1. Create & activate env:
```bash
conda create -n etl_demo python=3.10 -y
conda activate etl_demo
pip install -r requirements.txt