def detect_cycles(df):
    """
    Detect simple transaction cycles like:
    A → B → C → A
    """
    cycles = {}

    tx_map = {}
    for _, r in df.iterrows():
        tx_map.setdefault(r["SourceAccount"], set()).add(r["TargetAccount"])

    for a in tx_map:
        for b in tx_map.get(a, []):
            for c in tx_map.get(b, []):
                if a in tx_map.get(c, []):
                    cycle = f"{a}->{b}->{c}->{a}"
                    for acc in [a, b, c]:
                        cycles.setdefault(acc, []).append(cycle)

    return cycles