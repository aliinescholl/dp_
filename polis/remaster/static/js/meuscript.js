$(function() { 
    $(document).on("click", "#btIncluirPessoa", function() {
        //pegar dados da tela
        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();
        //console.log(nome, email, senha);

        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, email: email, senha: senha });
        $.ajax({
            url: 'http://localhost:5000/cadastro',
            type: 'POST',
            dataType: 'json', 
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, 
            success: pessoaIncluida, 
            error: erroAoIncluir
        });
        function pessoaIncluida (retorno) {
            if (retorno.resultado == "ok") {
                alert("Cadastro realizado com sucesso!");
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
            alert("Erro ao contatar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});
$(function() {
    $(document).on("click", "#btnFazerLogin", function() {
        //recebe os dados da tela
        email = $("#campoEmail").val();
        senha = $("#campoSenha").val();

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
            if (retorno.resultado == "ok") {
                alert("Login realizado com sucesso!");
                $("#campoEmail").val("");
                $("#campoSenha").val("");
            } else {
                alert("Erro no login: "+retorno.resultado + ":" + retorno.detalhes);
            }            
        }
        function erroaoLogar (retorno) {
            alert("Erro ao contatar back-end: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });
});



$(function () {

    $(document).on("click", "#btIncluirLivro", function () {
        var dados_foto = new FormData($('#formLivro')[0]);
        console.log('chegou aqui')
        $.ajax({
            url: 'http://localhost:5000/save_image',
            method: 'POST',
            data: dados_foto, // dados serão enviados em formato normal, para upload da foto
            contentType: false,
            cache: false,
            processData: false,
            success: function (data) {
                alert("enviou a foto direitinho!");
                insereLivroNoBanco();
            },
            error: function (data) {
                alert("deu ruim na foto, arruma ai");
            }
        });

        function insereLivroNoBanco() {

            //pegar dados da tela
            titulo = $("#CampoTitulo").val();
            autor = $("#CampoAutor").val();
            resumo = $("#CampoResumo").val();

            // C:\\fakepath\\olho.jpg"
            // esse fakepath vem de algum lugar da biblioteca utilizada
            // só conta a contrabarra uma vez, inicia do zero
            capa_livro = $("#FotoCapaLivro").val().substr(12);

            // preparar dados no formato json
            var dados = JSON.stringify({ titulo: titulo, autor: autor, resumo: resumo, capa_livro: capa_livro });
            // fazer requisição para o back-end
            $.ajax({
                url: 'http://localhost:5000/save_image',
                method: 'POST',
                dataType: 'json', // os dados são recebidos no formato json
                data: dados, // estes são os dados enviados
                success: livro_incluido, // chama a função listar para processar o resultado
                error: erroAoIncluirLivro
            });
            function livro_incluido(retorno) {
                if (retorno.resultado == "ok") {
                    alert("Livro cadastrado com sucesso");
                    $("#CampoTitulo").val();
                    $("#CampoAutor").val();
                    $("#CampoResumo").val();

                } else {
                    // informar mensagem de erro
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            }
            function erroAoIncluirLivro(retorno) {
                // informar mensagem de erro
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }

    });
});