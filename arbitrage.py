import pandas as pd

def detect_arbitrage(odds_data):
    # odds_data: list of dicts like {"book": "Betano", "team1": 2.1, "team2": 1.8}
    df = pd.DataFrame(odds_data)

    opportunities = []

    for event in df["event_id"].unique():
        market = df[df["event_id"] == event]
        if len(market) < 2:
            continue

        # Compute arbitrage percentage for 2-way market
        market["inv"] = 1 / market["odds"]
        arb_sum = market.groupby("outcome")["inv"].min().sum()
        if arb_sum < 1:
            profit = (1 - arb_sum) * 100
            opportunities.append({
                "event": event,
                "profit_%": round(profit, 2),
                "books": market[["book", "odds"]].to_dict(orient="records")
            })

    return opportunities
