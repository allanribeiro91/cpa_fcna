document.addEventListener('DOMContentLoaded', function() {
    var slider = document.getElementById("rangeSlider");
    var output = document.getElementById("sliderValue");
    slider.classList.remove("has-value"); // Inicialmente, remove a classe que indica um valor selecionado

    // Atualiza o valor mostrado quando o slider é movido
    slider.oninput = function() {
        output.innerHTML = "Valor selecionado: <b>" + this.value + "</b>";
        slider.classList.add("has-value"); // Indica que um valor foi selecionado
    }
});
