from configs.config import *
from configs.criptografia import *
from cadastro_pessoas.modelo import *

@app.route("/login_pessoa", methods=['POST'])
def login_pessoa():
    # preparar uma resposta otimista
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    # receber as informações do novo objeto
    dados = request.get_json(force=True)  
    login = dados['login']
    senha = dados['senha']

    # verificar se login e senha estão corretos
    encontrado = Pessoa.query.filter_by(email=login, senha=cifrar(senha)).first()
    if encontrado is not None:
        session[login] = "OK"
    else:
        resposta = jsonify({"resultado": "erro", "detalhes": "login e/ou senha inválido(s)"})        
    # adicionar cabeçalho de liberação de origem
    resposta.headers.add("Access-Control-Allow-Origin", meuservidor)
    # permitir envio do cookie
    resposta.headers.add("Access-Control-Allow-Credentials", "true")
    return resposta  # responder!