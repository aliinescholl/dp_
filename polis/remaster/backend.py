from config import *
from modelo import Pessoa
from flask_session import *
from flask_sqlalchemy import *
from flask import *
from flask_cors import *
import os

@app.route("/")
def inicio():
    return render_template('index.html')

#teste_rota: curl -d '{"email":"josilva@gmail.com", "senha":"1234567"}' -X POST" localhost:5000/fazer_login

@app.route('/cadastro', methods=['GET', 'POST'])
def incluir_pessoa():
    if request.method == 'GET':
        return render_template("cadastro.html")
    else:
        # preparar uma resposta otimista
        resposta = jsonify({"resultado": "ok", "detalhes": "oi"})
        # receber as informações da nova pessoa
        dados = request.get_json(force = True)  # (force=True) dispensa Content-Type na requisição
        try:  
            nova = Pessoa(**dados)  # criar a nova pessoa
            db.session.add(nova)  # adicionar no BD
            db.session.commit()  # efetivar a operação de gravação
        except Exception as e:  # em caso de erro...
            # informar mensagem de erro
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        # adicionar cabeçalho de liberação de origem
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta  # responder!

@app.route('/fazer_login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        dados = request.get_json(force=True)
        email = str(dados['email'])
        senha = str(dados['senha'])
        print(dados)

        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta  # responder!


app.run(debug=True, host='0.0.0.0', port=5000)
