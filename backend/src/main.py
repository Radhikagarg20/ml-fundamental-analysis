import pandas as pd
import numpy as np

from src.api.fetch_data import fetch_company_data
from src.processing.metrics_builder import build_metrics
from src.ml_engine.scoring import calculate_financial_score
from src.ml_engine.insight_generator import generate_insights
from src.ml_engine.classifier import FinancialClassifier
from src.database.db_manager import save_analysis


def run_pipeline(company_list):

    print("🚀 Financial Analysis Pipeline Started\n")

    classifier = FinancialClassifier()

    X_train = np.array([
        [18, 22, 19, 0.5, 30],
        [5, 7, 6, 2.5, 0],
        [12, 14, 10, 1.2, 10],
        [25, 28, 24, 0.3, 40],
        [6, 9, 8, 2.0, 2]
    ])

    y_train = [2, 0, 1, 2, 0]
    classifier.train(X_train, y_train)

    total = len(company_list)

    for count, company_id in enumerate(company_list, start=1):

        print(f"📊 Processing {company_id} ({count}/{total})")

        raw_data = fetch_company_data(company_id)

        if not raw_data:
            print("❌ API fetch failed")
            continue

        metrics = build_metrics(raw_data)

        score = calculate_financial_score(metrics)

        pros, cons = generate_insights(metrics)

        try:
            category = classifier.predict(metrics)
        except:
            category = "Unknown"

        try:
            save_analysis(company_id, score, pros, cons)
            print("💾 Saved to database")
        except Exception as e:
            print("⚠ Database save failed:", e)

        print("🧠 Category:", category)
        print("📈 Financial Score:", score)
        print("🟢 Pros:", pros)
        print("🔴 Cons:", cons)
        print("-" * 50)

    print("\n✅ Pipeline Completed Successfully!")


if __name__ == "__main__":

    try:
        excel_path = "../data/Nifty100Companies.xlsx"
        df = pd.read_excel(excel_path)
        companies = df.iloc[:, 0].dropna().tolist()
    except Exception:
        print("⚠ Excel not found, using default companies")
        companies = ["TCS", "HDFCBANK", "DMART"]

    run_pipeline(companies)