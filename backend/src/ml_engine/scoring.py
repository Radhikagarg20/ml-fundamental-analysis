def calculate_financial_score(metrics):

    score = 0

    # ROCE weight
    score += metrics["roe"] * 0.4

    # Growth weight
    score += metrics["sales_growth"] * 0.2
    score += metrics["profit_growth"] * 0.2

    # Dividend
    score += metrics["dividend_payout"] * 0.1

    # Penalize only if very high leverage
    if metrics["debt_to_equity"] > 2:
        score -= 10

    return round(score, 2)