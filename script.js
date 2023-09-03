const backToTopButton = document.getElementById("back-to-top-button");

window.addEventListener("scroll", () => {
  if (window.scrollY > window.innerHeight) {
    backToTopButton.classList.remove("hidden");
  } else {
    backToTopButton.classList.add("hidden");
  }
});

backToTopButton.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});
