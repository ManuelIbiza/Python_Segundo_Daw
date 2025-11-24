function conclusion() {
    console.log("Entramos en conclusión!");

    const conclusionP = document.getElementById("conclusion");
    const input = document.getElementById("texto1");

    // Usa la ruta absoluta de tu vista resultado
    fetch(`/app2/resultado/?texto1=${encodeURIComponent(input.value)}`)
        .then(r => r.text())
        .then(html => {
            conclusionP.innerHTML = html;
        })
        .catch(err => console.error(err));
}