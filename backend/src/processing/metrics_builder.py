import re


def safe_float(value):
    try:
        if value is None:
            return 0.0
        if isinstance(value, str):
            value = value.replace("%", "").replace(",", "").strip()
        return float(value)
    except:
        return 0.0


def extract_percentage(text):
    if not text:
        return 0.0
    match = re.search(r'(\d+(\.\d+)?)%', text)
    return float(match.group(1)) if match else 0.0


def build_metrics(raw_data):

    # 🔥 USE ROCE DIRECTLY (THIS EXISTS IN YOUR API)
    roe_value = raw_data.get("roce_percentage")

    metrics = {
        "roe": safe_float(roe_value),   # Always use ROCE
        "sales_growth": 0.0,
        "profit_growth": 0.0,
        "debt_to_equity": 0.0,
        "dividend_payout": 0.0,
    }

    # ---- Extract growth & dividend from prosandcons ----
    pros_cons = raw_data.get("data", {}).get("prosandcons", [])

    for item in pros_cons:
        pros_text = (item.get("pros") or "").lower()

        if "sales growth" in pros_text:
            metrics["sales_growth"] = extract_percentage(pros_text)

        if "profit growth" in pros_text:
            metrics["profit_growth"] = extract_percentage(pros_text)

        if "dividend payout" in pros_text:
            metrics["dividend_payout"] = extract_percentage(pros_text)

    # ---- Debt Ratio from Balance Sheet ----
    balancesheet = raw_data.get("data", {}).get("balancesheet", [])

    if isinstance(balancesheet, list) and balancesheet:
        latest = balancesheet[-1]

        borrowings = safe_float(latest.get("borrowings"))
        equity_capital = safe_float(latest.get("equity_capital"))
        reserves = safe_float(latest.get("reserves"))

        total_equity = equity_capital + reserves

        if total_equity > 0:
            metrics["debt_to_equity"] = round(borrowings / total_equity, 2)

    return metrics