function getQueryParam(param) {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

async function init() {

    const company = getQueryParam("company");
    if (!company) return;

    document.getElementById("companyName").innerText = company;

const data = await fetchAnalysis(company);

    document.getElementById("score").innerText = data.score;
    document.getElementById("roce").innerText = data.metrics.roe + "%";
    document.getElementById("salesGrowth").innerText = data.metrics.sales_growth + "%";
    document.getElementById("debt").innerText = data.metrics.debt_to_equity;

    const badge = document.getElementById("categoryBadge");
    badge.innerText = data.category;

    if (data.category === "Strong") {
        badge.className = "px-4 py-2 rounded-full bg-success shadow-glow";
    } else if (data.category === "Stable") {
        badge.className = "px-4 py-2 rounded-full bg-yellow-600";
    } else {
        badge.className = "px-4 py-2 rounded-full bg-danger";
    }

    const prosList = document.getElementById("prosList");
    prosList.innerHTML = "";
    data.pros.forEach(p => {
        const li = document.createElement("li");
        li.className = "text-green-400";
        li.innerText = "✔ " + p;
        prosList.appendChild(li);
    });

    const consList = document.getElementById("consList");
    consList.innerHTML = "";
    data.cons.forEach(c => {
        const li = document.createElement("li");
        li.className = "text-red-400";
        li.innerText = "✖ " + c;
        consList.appendChild(li);
    });

    renderChart(data.metrics);
}

init();