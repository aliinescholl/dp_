$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirPessoa", function() {

        var dados_foto = new FormData($('#meuform')[0]);

        $.ajax({
            url: 'http://localhost:5000/save_image',
            method: 'POST',
            //dataType: 'json',
            data: dados_foto, // dados serão enviados em formato normal, para upload da foto
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                alert("enviou a foto direitinho!");
                inserePessoaNoBanco();
            },
            error: function (data) {
                alert("deu ruim na foto");
            }
        });

        //pegar dados da tela
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();
        console.log(nome, email, senha);

        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, email: email, senha: senha });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_pessoa',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: pessoaIncluida, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Cadastro realizado com sucesso!");
                //$("#mensagem").text("Pessoa incluída com sucesso!");
                // limpar os campos
                $("#campoNome").val("");
                $("#campoEmail").val("");
                $("#campoSenha").val("");
            } else {
                // informar mensagem de erro
                alert("ERRO na inclusão: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});