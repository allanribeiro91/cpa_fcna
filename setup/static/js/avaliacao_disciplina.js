document.addEventListener('DOMContentLoaded', function() {
    
    //Verificar se há mensagem de salvamento com sucesso
    if (localStorage.getItem('formularioSalvo') === 'true') {
        sweetAlert('Formulário salvo com sucesso!', 'success', 'top-end');
        localStorage.removeItem('formularioSalvo');
    }


    //dados do formulário
    const elementoFormulario = document.getElementsByClassName('formulario')[0];
    const uuidFormulario = elementoFormulario.getAttribute('data-uuid-formulario');
    const uuidUsuario = elementoFormulario.getAttribute('data-uuid-usuario');
    
    
    const botao_voltar = document.getElementById('voltar')
    botao_voltar.addEventListener('click', function(){

        window.location.href = `/lista_avaliacoes/${uuidUsuario}/`;

    })


    // Suponha que você tenha 4 perguntas
    for (let i = 1; i <= 4; i++) {
        let pergunta = document.getElementById("pergunta" + i);
        let perguntaValor = document.getElementById("perguntaValor" + i);

        pergunta.oninput = function() {
            perguntaValor.innerHTML = "Valor selecionado: <b>" + this.value + "</b>";
            this.classList.add("has-value");
        };
    }



    const formularioDados = document.getElementById('formAvaliacaoDisciplina')
    const botao_salvar = document.getElementById('btnSalvar')
    botao_salvar.addEventListener('click', function(e){
        e.preventDefault();
        salvar_formulario();
        localStorage.setItem('formularioSalvo', 'true');
        window.location.reload();
    })


    function salvar_formulario(){
        // //Verificar preenchimento dos campos
        // let preenchimento_incorreto = verificar_campos()
        // if (preenchimento_incorreto === false) {
        //     return;
        // }

        //Enviar para o servidor
            //definir o caminho
            postURL = `/formularios/avaliacao_disciplina/${uuidFormulario}/`

            //pegar os dados
            let formData = new FormData(document.getElementById('formAvaliacaoDisciplina'));
    
            //enviar 
            fetch(postURL, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
        
    }

    

});
