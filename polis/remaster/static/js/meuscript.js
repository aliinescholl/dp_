$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirPessoa", function() {
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
                alert("Erro no cadastro, por favor contate o administrador " + retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroAoIncluir (retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: "+retorno.resultado + ":" + retorno.detalhes);
        }
    });
});
$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão
    $(document).on("click", "#btnFazerLogin", function() {
        //recebe os dados da tela
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();
        //console.log(email, senha); 

        var dados = JSON.stringify({ email: email, senha: senha });//compila os dados todos juntos em json
        $.ajax({
            url: 'http://localhost:5000/fazer_login',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, 
            success: loginFeito, 
            error: erroaoLogar
        });
        function loginFeito (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                alert("Login realizado com sucesso!");
                // limpar os campos
                $("#campoEmail").val("");
                $("#campoSenha").val("");
            } else {
                // informar mensagem de erro
                alert("ERRO no login: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroaoLogar (retorno) {
            // informar mensagem de erro
            alert("ERRO ao contactar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});
