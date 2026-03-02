import pandas as pd
import random
from datetime import datetime
import threading
import time
import os

CSV_PATH = "data/transactions.csv"

ACCOUNTS = [f"ACC_{i:03d}" for i in range(1, 51)]
CHANNELS = ["UPI", "NetBanking", "PaymentGateway", "MobileApp"]

def add_synthetic_record():
    src = random.choice(ACCOUNTS)
    tgt = random.choice([a for a in ACCOUNTS if a != src])
    channel = random.choice(CHANNELS)

    # amount ALWAYS ends with .0
    amount = float(random.randint(100, 100000))

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

    new_row = pd.DataFrame([{
        "SourceAccount": src,
        "TargetAccount": tgt,
        "Channel": channel,
        "Amount": amount,
        "Timestamp": timestamp
    }])

    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        df = pd.concat([df, new_row], ignore_index=True)
    else:
        df = new_row

    df.to_csv(CSV_PATH, index=False)

def start_periodic_generation(interval_seconds=300):
    def run():
        while True:
            add_synthetic_record()
            time.sleep(interval_seconds)

    thread = threading.Thread(target=run, daemon=True)
    thread.start()