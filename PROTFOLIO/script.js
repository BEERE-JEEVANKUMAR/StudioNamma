const btn = document.querySelector(".btn");
btn.addEventListener("click", () => {
    alert("Thank you for visiting my portfolio!");
});
const cards = document.querySelectorAll(".card");
cards.forEach(card => {
    card.addEventListener("mouseenter", () => {
        card.style.background = "#eaf4ff";
    });
    card.addEventListener("mouseleave", () => {
        card.style.background = "white";
    });
});