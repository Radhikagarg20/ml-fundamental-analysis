const API_BASE = "https://ml-fundamental-analysis.onrender.com";

async function fetchAnalysis(company) {
    try {
        const response = await fetch(`${API_BASE}/analyze?id=${company}`);

        if (!response.ok) {
            throw new Error("Backend error");
        }

        return await response.json();
    } catch (error) {
        console.error(error);
        alert("Failed to connect to backend.");
    }
}