from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.nome + ", " +\
            self.email + ", " + self.senha
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }

def pegar_email_no_bd(email_bd:str):
    return Pessoa.query.get(email_bd)

def ver_senha_no_bd(email_bd:str, senha:str):
    for q in db.session.query(Pessoa.senha).filter(Pessoa.email_bd).all:
        if q == None:
            return False
        return 