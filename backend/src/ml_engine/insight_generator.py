def generate_insights(metrics):

    pros = []
    cons = []

    if metrics["roe"] > 20:
        pros.append(f"Strong ROCE of {metrics['roe']}%")
    else:
        cons.append(f"Low ROCE of {metrics['roe']}%")

    if metrics["sales_growth"] > 10:
        pros.append(f"Healthy sales growth of {metrics['sales_growth']}%")
    else:
        cons.append(f"Poor sales growth of {metrics['sales_growth']}%")

    if metrics["dividend_payout"] > 20:
        pros.append(f"Consistent dividend payout of {metrics['dividend_payout']}%")

    if metrics["debt_to_equity"] > 2:
        cons.append("High debt burden")

    return pros[:3], cons[:3]