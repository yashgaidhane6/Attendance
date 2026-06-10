document.addEventListener("DOMContentLoaded", () => {

    // Dashboard Cards Animation
    const cards = document.querySelectorAll(".card");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";

        setTimeout(() => {

            card.style.transition = "all 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";

        }, index * 200);

    });

    // Table Row Animation
    const rows = document.querySelectorAll("table tr");

    rows.forEach((row, index) => {

        row.style.opacity = "0";

        setTimeout(() => {

            row.style.transition = "0.5s";
            row.style.opacity = "1";

        }, index * 100);

    });

    // Auto Hide Alerts
    const alertBox = document.querySelector(".alert");

    if (alertBox) {

        setTimeout(() => {

            alertBox.style.transition = "0.5s";
            alertBox.style.opacity = "0";

            setTimeout(() => {
                alertBox.remove();
            }, 500);

        }, 3000);

    }

    // Button Click Animation
    const buttons = document.querySelectorAll("button");

    buttons.forEach(button => {

        button.addEventListener("click", () => {

            button.style.transform = "scale(0.95)";

            setTimeout(() => {
                button.style.transform = "scale(1)";
            }, 150);

        });

    });

});
