from flask import Flask, jsonify, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import os

from flask_cors import CORS # permitir back receber json do front

# configurações
app = Flask(__name__)
meuservidor = "http://localhost:8080"
CORS(app) # aplicar o cross domain
# caminho do arquivo de banco de dados
path = os.path.dirname(os.path.abspath(__file__)) 
arquivobd = os.path.join(path, 'pessoas.db')
# sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///"+arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # remover warnings
db = SQLAlchemy(app)

app.secret_key = '$#EWFGHJUI*&DEGBHYJU&Y%T#RYJHG%##RU&U'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)