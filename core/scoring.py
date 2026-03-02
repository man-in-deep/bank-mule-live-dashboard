def compute_mule_scores(scenario_map):
    scores = {}

    for acc, scenarios in scenario_map.items():
        score = round(len(scenarios) / 10, 2)
        is_mule = score >= 0.4

        scores[acc] = {
            "mule_score": score,
            "is_mule": is_mule,
            "scenarios": scenarios
        }

    return scores