import pandas as pd

CSV_PATH = "data/transactions.csv"

def load_transactions():
    df = pd.read_csv(CSV_PATH)

    # microseconds-safe timestamp parsing
    df["Timestamp"] = pd.to_datetime(
        df["Timestamp"],
        format="mixed",
        errors="coerce"
    )

    df = df.dropna(subset=["Timestamp"])
    return df