$(function() { // quando o documento estiver pronto/carregado
    
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btIncluirLivro", function() {
        //pegar dados da tela
        titulo = $("#campoTitulo").val();
        descricao = $("#campoDescricao").val();
        autor = $("#campoAutor").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ titulo: titulo, descricao: descricao, autor: autor });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/incluir_livro',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: livroIncluido, // chama a função listar para processar o resultado
            error: erroAoIncluir
        });
        function livroIncluido (retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Livro incluído com sucesso!");
                //$("#mensagem").text("Pessoa incluída com sucesso!");
                // limpar os campos
                $("#campoTitulo").val("");
                $("#campoDescricao").val("");
                $("#campoAutor").val("");
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