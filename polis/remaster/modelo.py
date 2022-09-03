from config import *

class Pessoa(db.Model):# atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.Text)

    def __str__(self):
        return str(self.id)+ self.nome + ", " +\
            self.email + ", " + self.senha #expressar a pessoa em forma de texto

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        } # expressao da classe no formato json

def pegar_email_no_bd(email_bd:str):
    return Pessoa.query.get(email_bd)

def ver_senha_no_bd(email_bd:str, senha:str):
    for q in db.session.query(Pessoa.senha).filter(Pessoa.email_bd).all:
        if q == None:
            return False
        return

class Livro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_autor = db.Column(db.String(254))
    nome_livro = db.Column(db.String(254))
    resumo = db.Column(db.String(254))
    nome_foto = db.Column(db.Text)
    
    def __str__(self):
        return str(id) + self.nome_autor + ', ' + self.nome_livro + ', ' +\
            self.resumo + ', ' + self.nome_foto
    
    def json(self):
        return { 
            "id": self.id,
            "nome_autor": self.nome_autor,
            "nome_livro": self.nome_livro,
            "resumo": self.resumo,
            "nome_foto": self.nome_foto,
            }
           