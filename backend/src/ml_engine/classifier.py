from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import numpy as np

class FinancialClassifier:
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        self.is_trained = False

    def prepare_features(self, metrics):
        """
        Convert metrics dictionary into feature array
        """
        return np.array([
            metrics["roe"],
            metrics["sales_growth"],
            metrics["profit_growth"],
            metrics["debt_to_equity"],
            metrics["dividend_payout"]
        ]).reshape(1, -1)

    def train(self, X, y):
        """
        Train model on dataset
        """
        X_scaled = self.scaler.fit_transform(X)
        self.model.fit(X_scaled, y)
        self.is_trained = True

    def predict(self, metrics):
        """
        Predict category for a company
        """
        if not self.is_trained:
            raise Exception("Model not trained yet")

        X = self.prepare_features(metrics)
        X_scaled = self.scaler.transform(X)

        prediction = self.model.predict(X_scaled)[0]

        categories = {
            0: "Risky",
            1: "Stable",
            2: "Strong"
        }

        return categories.get(prediction, "Unknown")