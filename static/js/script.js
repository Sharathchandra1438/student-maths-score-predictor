// ==========================================
// PAGE LOADED
// ==========================================

document.addEventListener("DOMContentLoaded", function () {

    console.log("Student Performance App Loaded");


    // ==========================================
    // FORM VALIDATION
    // ==========================================

    const form = document.querySelector("form");

    form.addEventListener("submit", function (event) {

        // Get input values
        const readingScore = document.querySelector(
            'input[name="reading_score"]'
        ).value;

        const writingScore = document.querySelector(
            'input[name="writing_score"]'
        ).value;


        // ==========================================
        // VALIDATE EMPTY VALUES
        // ==========================================

        if (readingScore === "" || writingScore === "") {

            alert("Please fill all score fields.");

            event.preventDefault();

            return;
        }


        // ==========================================
        // VALIDATE SCORE RANGE
        // ==========================================

        if (
            readingScore < 0 ||
            readingScore > 100 ||

            writingScore < 0 ||
            writingScore > 100
        ) {

            alert("Scores must be between 0 and 100.");

            event.preventDefault();

            return;
        }


        // ==========================================
        // LOADING MESSAGE
        // ==========================================

        const button = document.querySelector("button");

        button.innerHTML = "Predicting...";

        button.disabled = true;
    });


    // ==========================================
    // INPUT ANIMATION EFFECT
    // ==========================================

    const inputs = document.querySelectorAll(
        "input, select"
    );

    inputs.forEach((input) => {

        input.addEventListener("focus", () => {

            input.style.transform = "scale(1.02)";

            input.style.transition = "0.2s";
        });

        input.addEventListener("blur", () => {

            input.style.transform = "scale(1)";
        });
    });
});