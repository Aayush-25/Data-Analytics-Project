# generate_data.py
import csv
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

OUT = Path("raw_data/orders.csv")
OUT.parent.mkdir(parents=True, exist_ok=True)

NUM = int(sys.argv[1]) if len(sys.argv) > 1 else 10000

cities = ["Delhi", "Mumbai", "Bangalore", "Pune", "Hyderabad", "Chennai", "Kolkata", "Ahmedabad"]
payment_types = ["card", "upi", "cash", "netbanking"]
statuses = ["delivered", "cancelled", "returned"]

start_date = datetime(2023, 1, 1)
def rand_date():
    delta = timedelta(days=random.randint(0, 365), hours=random.randint(0,23), minutes=random.randint(0,59))
    return (start_date + delta).strftime("%Y-%m-%d %H:%M:%S")

with OUT.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id","user_id","order_date","item_id","item_price","qty","city","payment_type","order_status"])
    for i in range(1, NUM+1):
        order_id = f"o{i}"
        user_id = f"u{random.randint(1, max(2, NUM//10))}"
        order_date = rand_date()
        item_id = f"i{random.randint(1,200)}"
        item_price = round(random.uniform(10, 2000), 2)
        qty = random.randint(1, 5)
        city = random.choice(cities)
        payment_type = random.choice(payment_types)
        status = random.choices(statuses, weights=[85,10,5], k=1)[0]
        writer.writerow([order_id, user_id, order_date, item_id, item_price, qty, city, payment_type, status])

print(f"Wrote {NUM} rows to {OUT}")