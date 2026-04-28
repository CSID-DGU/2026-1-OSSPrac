const themeToggle = document.getElementById("themeToggle");
const themeIcon = document.getElementById("themeIcon");
const themeText = document.getElementById("themeText");

function applyTheme(theme) {
    document.documentElement.setAttribute("data-bs-theme", theme);
    localStorage.setItem("theme", theme);

    if (theme === "dark") {
        themeIcon.className = "bi bi-sun me-1";
        themeText.textContent = "Light";
    } else {
        themeIcon.className = "bi bi-moon-stars me-1";
        themeText.textContent = "Dark";
    }
}

const currentTheme = localStorage.getItem("theme") || "light";
applyTheme(currentTheme);

themeToggle.addEventListener("click", () => {
    const activeTheme = document.documentElement.getAttribute("data-bs-theme");
    const nextTheme = activeTheme === "dark" ? "light" : "dark";
    applyTheme(nextTheme);
});