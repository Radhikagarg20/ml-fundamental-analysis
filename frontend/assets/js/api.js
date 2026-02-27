const API_BASE = "https://ml-fundamental-analysis.onrender.com";

async function fetchAnalysis(company) {
    try {
        const response = await fetch(`${API_BASE}/analyze?id=${company}`);

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        if (data.error) {
            alert(data.error);
            return null;
        }

        return data;

    } catch (error) {
        console.error("Fetch error:", error);
        alert("Failed to connect to backend.");
        return null;
    }
}