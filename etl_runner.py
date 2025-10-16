# src/etl_runner.py
import time, logging, os
from src.extract import extract_csv
from src.transform import transform
from src.load import upsert_orders
from sqlalchemy import create_engine, text

logging.basicConfig(level=logging.INFO)
DB_URL = os.environ.get("DATABASE_URL", "sqlite:///./etl_demo.db")
engine = create_engine(DB_URL, future=True)

def record_run(rows_extracted, rows_loaded, runtime_seconds, errors=0):
    with engine.begin() as conn:
        conn.execute(text(
            "INSERT INTO etl_runs (rows_extracted, rows_loaded, runtime_seconds, errors) VALUES (:re, :rl, :rt, :err)"
        ), {"re": rows_extracted, "rl": rows_loaded, "rt": runtime_seconds, "err": errors})

def run_etl(path="raw_data/orders.csv"):
    start = time.time()
    raw = extract_csv(path)
    rows_extracted = len(raw)
    try:
        df = transform(raw)
        rows_loaded = len(df)
        upsert_orders(df)
        runtime = int(time.time() - start)
        record_run(rows_extracted, rows_loaded, runtime, errors=0)
        logging.info(f"ETL done. Extracted {rows_extracted}, Loaded {rows_loaded}, runtime {runtime}s")
    except Exception as e:
        runtime = int(time.time() - start)
        record_run(rows_extracted, 0, runtime, errors=1)
        logging.exception("ETL failed")
        raise

if __name__ == "__main__":
    run_etl()