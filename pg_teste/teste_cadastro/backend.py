from config import *
from modelo import Usuario

@app.route("/")

def inicio():
    return "Sistema de cadastro dos Usuários" +\
        '<a href="/incluir">Operação incluir pessoa</a>'

@app.route("/incluir_usuario", method=['post'])
def incluir_usuario():
    resposta = jsonify({"resultado": "ok", "detalhes": "oi"})

    dados = request.get_json()

    try:  # tentar executar a operação
        nova = Usuario(**dados)  # criar a nova pessoa
        db.session.add(nova)  # adicionar no BD
        db.session.commit()  # efetivar a operação de gravação
    except Exception as e:  # em caso de erro...
        # informar mensagem de erro
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta #responder no consoler

app.run(debug=True)