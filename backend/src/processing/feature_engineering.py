import re

def safe_float(value):
    try:
        if value is None:
            return 0.0
        if isinstance(value, str):
            value = value.replace("%", "").strip()
        return float(value)
    except:
        return 0.0


def extract_percentage_from_text(text):
    match = re.search(r'(\d+(\.\d+)?)%', text)
    if match:
        return float(match.group(1))
    return 0.0


def extract_key_metrics(raw_data):

    metrics = {
        "roe": safe_float(raw_data.get("roce_percentage")),  # use ROCE
        "sales_growth": 0.0,
        "profit_growth": 0.0,
        "debt_to_equity": 0.0,
        "dividend_payout": 0.0,
    }

    # Extract from prosandcons
    pros_cons = raw_data.get("data", {}).get("prosandcons", [])

    for item in pros_cons:
        pros_text = item.get("pros", "") or ""
        cons_text = item.get("cons", "") or ""

        if "sales growth" in pros_text.lower():
            metrics["sales_growth"] = extract_percentage_from_text(pros_text)

        if "profit growth" in pros_text.lower():
            metrics["profit_growth"] = extract_percentage_from_text(pros_text)

        if "dividend payout" in pros_text.lower():
            metrics["dividend_payout"] = extract_percentage_from_text(pros_text)

    # Debt ratio from balancesheet
    balancesheet = raw_data.get("data", {}).get("balancesheet", [])

    if balancesheet:
        latest = balancesheet[-1]
        borrowings = safe_float(latest.get("borrowings"))
        equity = safe_float(latest.get("equity_capital"))

        if equity != 0:
            metrics["debt_to_equity"] = borrowings / equity

    return metrics