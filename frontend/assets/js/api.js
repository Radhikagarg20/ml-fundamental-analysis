const BASE_URL = "https://ml-fundamental-analysis.onrender.com";

async function fetchAnalysis(company) {
    const response = await fetch(`${BASE_URL}/analyze?id=${company}`);
    return await response.json();
}