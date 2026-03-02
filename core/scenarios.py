from collections import defaultdict
from core.cycles import detect_cycles

def run_all_scenarios(df):
    results = defaultdict(set)

    # Scenario 1: High daily volume
    daily = df.groupby("SourceAccount")["Amount"].sum()
    for acc, amt in daily.items():
        if amt > 500000:
            results[acc].add("HIGH_DAILY_OUTFLOW")

    # Scenario 2: Many unique targets
    targets = df.groupby("SourceAccount")["TargetAccount"].nunique()
    for acc, cnt in targets.items():
        if cnt >= 5:
            results[acc].add("MULTIPLE_TARGETS")

    # Scenario 3: Rapid back-and-forth
    for _, r in df.iterrows():
        mask = (
            (df["SourceAccount"] == r["TargetAccount"]) &
            (df["TargetAccount"] == r["SourceAccount"])
        )
        if mask.any():
            results[r["SourceAccount"]].add("ROUND_TRIP")

    # Scenario 4–9 placeholders (already counted in DROP 1 logic)
    for acc in df["SourceAccount"].unique():
        if df[df["SourceAccount"] == acc].shape[0] >= 10:
            results[acc].add("HIGH_TX_COUNT")

    # Scenario 10: Cycle detection
    cycles = detect_cycles(df)
    for acc, cyc in cycles.items():
        results[acc].add("MONEY_CYCLE")

    return {k: list(v) for k, v in results.items()}