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


├── Dockerfile
├── README.md
├── create_db.py
├── docker-compose.yml
├── etl_demo.db
├── init_db.sql
├── raw_data
│   ├── generate_data.py
│   └── orders.csv
├── requirements.txt
└── src
    ├── __pycache__
    ├── app.py
    ├── etl_runner.py
    ├── extract.py
    ├── load.py
    └── transform.py
