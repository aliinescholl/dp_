from configs.config import *
from modelo import Livrinho

@app.route("/")
def inicio():
    return 'Sistema de cadastro de pessoas. '+\
        '<a href="/incluir">Operação incluir Livro</a>'

@app.route("/save_image", methods=['POST'])
def salvar_imagem():
    try:
        print("comecando")
        file_val = request.files['foto']
        print("vou salvar em: "+file_val.filename)
        arquivoimg = os.path.join(caminho, 'imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

@app.route('/get_image/<int:id_livro>')
def get_image(id_livro):
    catalogo = db.session.query(Livrinho).get(id_livro)
    arquivoimg = os.path.join(caminho, 'imagens/'+ catalogo.nome_foto)
    return send_file(arquivoimg, mimetype='image/gif')

# teste da rota: curl -d '{"nome":"James Kirk", "telefone":"92212-1212", "email":"jakirk@gmail.com"}' -X POST -H "Content-Type:application/json" localhost:5000/incluir_pessoa
@app.route("/incluir_livro", methods=['post'])
def incluir_livro():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
    # receber as informações da nova pessoa
    dados = request.get_json() #(force=True) dispensa Content-Type na requisição
    try: # tentar executar a operação
      novo = Livrinho(**dados) # criar a nova pessoa
      db.session.add(novo) # adicionar no BD
      db.session.commit() # efetivar a operação de gravação
    except Exception as e: # em caso de erro...
      # informar mensagem de erro
      resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta # responder!

app.run(debug=True)