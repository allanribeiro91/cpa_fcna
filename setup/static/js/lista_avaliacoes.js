document.addEventListener('DOMContentLoaded', function() {

    var cards = document.querySelectorAll(".card-avaliacao")

    cards.forEach(function(card) {
        card.addEventListener('click', function() {
            
            const formulario = $(this).attr('data-formulario').toString();
            const id_formulario = $(this).attr('data-id').toString();
            

            window.location.href = '/formularios/avaliacao_disciplina/'

        });
    });

});