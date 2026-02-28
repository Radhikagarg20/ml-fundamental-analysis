from flask import Flask, request, jsonify
from flask_cors import CORS

from src.api.fetch_data import fetch_company_data
from src.processing.metrics_builder import build_metrics
from src.ml_engine.scoring import calculate_financial_score
from src.ml_engine.insight_generator import generate_insights

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

def classify_score(score):
    if score > 30:
        return "Strong"
    elif score > 15:
        return "Stable"
    else:
        return "Risky"


@app.route("/")
def home():
    return {
        "status": "ML Fundamental Analysis API Running 🚀"
    }


@app.route("/analyze")
def analyze():

    company_id = request.args.get("id")

    if not company_id:
        return jsonify({"error": "Please provide company id like ?id=TCS"}), 400

    raw_data = fetch_company_data(company_id)

    if not raw_data:
        return jsonify({"error": "API fetch failed"}), 500

    metrics = build_metrics(raw_data)
    score = calculate_financial_score(metrics)
    pros, cons = generate_insights(metrics)
    category = classify_score(score)

    return jsonify({
        "company": company_id,
        "score": score,
        "category": category,
        "metrics": metrics,
        "pros": pros,
        "cons": cons
    })


if __name__ == "__main__":
    app.run(debug=True)