document.addEventListener('DOMContentLoaded', function() {

    $('#cpf').mask('000.000.000-00')


    

    const cpf = document.getElementById('cpf')
    cpf.addEventListener('change', function(){
        var cpf_usuario = cpf.value.replace(/\D/g, '');
        var cpf_valido = validaCPF(cpf_usuario)
        
        if (cpf_valido == false){
            var mensagem = '<span style="font-weight: normal">CPF: ' + cpf.value + ' <br><b style="color: red">INVÁLIDO!</b></span>'
            sweetAlert(mensagem)
            cpf.value = ''
        }
    })

    const dataNascimento = document.getElementById('data_nascimento')


    const botaoEntrar = document.getElementById('botaoEntrar')
    botaoEntrar.addEventListener('click', function(e){
        e.preventDefault();

        if (cpf.value == '') {
            var mensagem = '<span style="font-size: 24px; font-weight: normal">Informe o <b>CPF</b></span>'
            sweetAlert(mensagem)
            return
        }


        if (dataNascimento.value == '') {
            var mensagem = '<span style="font-size: 24px;font-weight: normal">Informe a<br> <b>Data de Nascimento</b></span>'
            sweetAlert(mensagem)
            return
        }

        verificarUsuario(cpf.value, dataNascimento.value)

    })

    function verificarUsuario(cpf, dataNascimento) {
        const url = `/verificar_usuario/${cpf}/${dataNascimento}/`;
    
        fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.verificacao === false) {
                var mensagem = `<span style="font-size: 24px;font-weight: normal">Usuário ${cpf} <br><b style="color: red">não encontrado!</b></span>`;
                sweetAlert(mensagem);
            } else {
                const usuarioUUID = data.usuario_uuid;
                // Correção: Use backticks para interpolação de strings
                window.location.href = `/lista_avaliacoes/${usuarioUUID}/`;
                // window.location.href = "/lista_avaliacoes/"
            }
        })
        .catch(error => console.error('Erro:', error));
    }

});