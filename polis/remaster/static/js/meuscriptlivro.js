

$(function () {

    $(document).on("click", "#btIncluirLivro", function () {
        var dados_foto = new FormData($('#formLivro')[0]);
        console.log(dados_foto)
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
            capa_livro = $("#FotoCapaLivro").val().substr(12);

            var dados = JSON.stringify({ titulo: titulo, autor: autor, resumo: resumo, capa_livro: capa_livro });
            $.ajax({
                url: 'http://localhost:5000/save_image',
                method: 'POST',
                dataType: 'json', 
                data: dados, 
                success: livro_incluido, 
                error: erroAoIncluirLivro
            });
            function livro_incluido(retorno) {
                if (retorno.resultado == "ok") {
                    alert("Livro cadastrado com sucesso");
                    $("#CampoTitulo").val();
                    $("#CampoAutor").val();
                    $("#CampoResumo").val();
                    $("#FotoCapaLivro").val();

                    $ajax

                } else {
                    // informar mensagem de erro
                    alert(retorno.resultado + ":" + retorno.detalhes);
                }
            }

            function erroAoIncluirLivro(retorno) {
                alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
            }
        }

    });
});