// 🌙 Dark/Light mode toggle with no flash
document.addEventListener("DOMContentLoaded", function() {
  const toggleBtn = document.getElementById("theme-toggle");
  const root = document.documentElement;

  const savedTheme = localStorage.getItem("theme");
  if (savedTheme === "dark") {
    root.classList.add("dark");
  }

  toggleBtn?.addEventListener("click", () => {
    root.classList.toggle("dark");

    if (root.classList.contains("dark")) {
      localStorage.setItem("theme", "dark");
      toggleBtn.textContent = "☀️";
    } else {
      localStorage.setItem("theme", "light");
      toggleBtn.textContent = "🌙";
    }
  });

  // Set correct icon
  toggleBtn.textContent = root.classList.contains("dark") ? "☀️" : "🌙";
});
