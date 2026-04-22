
document.addEventListener("DOMContentLoaded", () => {
    console.log("Game Platform Loaded");

    animateCards();
});



function animateCards() {
    const cards = document.querySelectorAll(".game-card");

    cards.forEach((card, index) => {
        card.style.opacity = 0;
        card.style.transform = "translateY(20px)";

        setTimeout(() => {
            card.style.transition = "0.4s";
            card.style.opacity = 1;
            card.style.transform = "translateY(0)";
        }, index * 120);
    });
}



function showLoading(gameName) {

    const container = document.querySelector(".container");

    container.innerHTML = `
        <div class="game-screen">
            <h2>Loading ${gameName}...</h2>
            <p>Please wait...</p>
        </div>
    `;

}



function confirmExit() {
    return confirm("Exit the Game Platform?");
}



document.addEventListener("click", function(e) {
    if (e.target.classList.contains("button")) {
        e.target.style.transform = "scale(0.95)";
        setTimeout(() => {
            e.target.style.transform = "scale(1)";
        }, 120);
    }
});