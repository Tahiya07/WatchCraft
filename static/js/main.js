// Dark/Light mode toggle
document.addEventListener("DOMContentLoaded", function() {
    const toggleBtn = document.getElementById("theme-toggle");
    toggleBtn?.addEventListener("click", () => {
        document.body.classList.toggle("dark");
    });
});
