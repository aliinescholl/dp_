from config import *

class Pessoa(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.Text)
    nome_foto = db.Column(db.Text)

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") " + self.nome + ", " +\
            self.email + ", " + self.senha + ", " + self.nome_foto
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "nome_foto": self.nome_foto
        }

# teste


def testar_pessoa():
    # teste da classe Pessoa
    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com",
                senha="1234567")

    # persistir
    db.session.add(p1)
    db.session.commit()

    # exibir a pessoa
    print(p1)

    # exibir a pessoa no format json
    print(p1.json())
