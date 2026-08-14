const appRoutes = {
    trx: {
        title: "TRX",
        file: "Pages/TRX.html"
    },
    parallels: {
        title: "Parallels Desktop",
        file: "Pages/Parallels.html"
    },
    vmware: {
        title: "VMWare Fusion",
        file: "Pages/VMWare.html"
    }
};

const homeView = document.getElementById("home-view");
const pageView = document.getElementById("page-view");

function showHome() {
    if (homeView) homeView.hidden = false;
    if (pageView) {
        pageView.hidden = true;
        pageView.innerHTML = "";
    }
    window.scrollTo({ top: 0, behavior: "auto" });
}

function buildBackButton() {
    const backButton = document.createElement("button");
    backButton.type = "button";
    backButton.className = "back-button";
    backButton.textContent = "Back";
    backButton.addEventListener("click", () => {
        showHome();
        window.location.hash = "";
    });
    return backButton;
}

function renderPageShell(content) {
    if (!pageView) return;

    const shell = document.createElement("div");
    shell.className = "page-shell";
    shell.appendChild(buildBackButton());

    const contentWrap = document.createElement("div");
    contentWrap.innerHTML = content;
    shell.appendChild(contentWrap);

    pageView.innerHTML = "";
    pageView.appendChild(shell);
}

async function loadPage(pageKey) {
    const route = appRoutes[pageKey];

    if (!route) {
        showHome();
        return;
    }

    if (homeView) homeView.hidden = true;
    if (pageView) {
        pageView.hidden = false;
        pageView.innerHTML = "<p class='loading'>Loading...</p>";
    }

    try {
        if (route.file) {
            const response = await fetch(route.file + "?v=" + Date.now());
            const html = await response.text();
            const doc = new DOMParser().parseFromString(html, "text/html");
            const bodyContent = doc.body.innerHTML || "<p>Content not found.</p>";

            renderPageShell(bodyContent);
            return;
        }

        renderPageShell(`<h2>${route.title}</h2>${route.content}`);
    } catch (error) {
        renderPageShell(`<h2>${route.title}</h2><p>Unable to load this page.</p>`);
    }
}

document.querySelectorAll(".buttonPage").forEach((button) => {
    button.addEventListener("click", () => {
        const pageKey = button.dataset.page;
        if (pageKey) {
            window.location.hash = pageKey;
            loadPage(pageKey);
        }
    });
});

window.addEventListener("hashchange", () => {
    const pageKey = window.location.hash.replace("#", "");
    if (pageKey) {
        loadPage(pageKey);
    } else {
        showHome();
    }
});

const initialPage = window.location.hash.replace("#", "");
if (initialPage) {
    loadPage(initialPage);
} else {
    showHome();
}
