function showLoader() {
    const loader = document.createElement("div");
    loader.id = "globalLoader";
    loader.innerHTML = `
        <div class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-80 z-50">
            <div class="w-16 h-16 border-4 border-blue-500 border-t-transparent rounded-full animate-spin"></div>
        </div>
    `;
    document.body.appendChild(loader);
}

function hideLoader() {
    const loader = document.getElementById("globalLoader");
    if (loader) loader.remove();
}

function fadeInPage() {
    document.body.classList.add("animate-fadeIn");
}

window.addEventListener("load", fadeInPage);