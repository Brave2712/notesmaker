const toggleBtn = document.getElementById("themeToggle");

if(toggleBtn){
    toggleBtn.addEventListener("click", () => {
        document.body.classList.toggle("light-mode");

        if(document.body.classList.contains("light-mode")){
            toggleBtn.innerHTML = "☀️ Light";
        }else{
            toggleBtn.innerHTML = "🌙 Dark";
        }
    });
}
