const API_BASE = "https://ml-fundamental-analysis.onrender.com";

async function fetchAnalysis(company) {
    try {
        const response = await fetch(`${API_BASE}/analyze?id=${company}`);

        if (!response.ok) {
            throw new Error("Backend error");
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error("Backend connection failed:", error);
        alert("Failed to connect to backend.");
    }
}