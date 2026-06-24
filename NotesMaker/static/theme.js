const toggleBtn = document.getElementById("themeToggle");

function applyTheme(theme){

    if(theme === "light"){
        document.body.classList.add("light-mode");
    }
    else{
        document.body.classList.remove("light-mode");
    }

}

const savedTheme = localStorage.getItem("theme") || "dark";

applyTheme(savedTheme);

if(toggleBtn){

    toggleBtn.addEventListener("click", () => {

        const newTheme =
            document.body.classList.contains("light-mode")
            ? "dark"
            : "light";

        localStorage.setItem("theme", newTheme);

        applyTheme(newTheme);

    });

}
