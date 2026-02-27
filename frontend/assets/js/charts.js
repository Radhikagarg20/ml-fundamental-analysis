function renderChart(metrics) {

    const ctx = document.getElementById("metricsChart").getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["ROCE", "Sales Growth", "Debt/Equity", "Dividend"],
            datasets: [{
                label: "Financial Metrics",
                data: [
                    metrics.roe,
                    metrics.sales_growth,
                    metrics.debt_to_equity,
                    metrics.dividend_payout
                ],
                backgroundColor: [
                    "#3B82F6",
                    "#10B981",
                    "#EF4444",
                    "#F59E0B"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: "white" }
                }
            },
            scales: {
                x: { ticks: { color: "white" }},
                y: { ticks: { color: "white" }}
            }
        }
    });
}