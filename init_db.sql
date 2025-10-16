-- init_db.sql (SQLite compatible)
CREATE TABLE IF NOT EXISTS orders (
    order_id TEXT PRIMARY KEY,
    user_id TEXT,
    order_date TEXT,
    item_id TEXT,
    item_price REAL,
    qty INTEGER,
    total_price REAL,
    city TEXT,
    payment_type TEXT,
    order_status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS etl_runs (
    run_id INTEGER PRIMARY KEY AUTOINCREMENT,
    run_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rows_extracted INTEGER,
    rows_loaded INTEGER,
    runtime_seconds INTEGER,
    errors INTEGER
);