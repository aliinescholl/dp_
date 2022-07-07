from configs.config import *
from cadastro_pessoas.modelo import *


class Postagem(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship("Pessoa")
    opiniao = db.Column(db.String(254))
    nota = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.pessoa) + ", " + self.opiniao + ', ' + self.nota
    # expressao da classe no formato json

    def json(self):
        return {
            "id": self.id,
            "pessoa": self.pessoa.json(),
            "opiniao": self.opiniao,
            'nota': self.nota
        }


# teste postagem

def testar_postagem():

    p1 = Pessoa(nome="João da Silva", email="josilva@gmail.com",
                senha="47 99012 3232")
    # teste da classe Postagem
    p2 = Postagem(pessoa=p1, opiniao="pessimo livro", nota='5')

    # persistir
    db.session.add(p1)
    db.session.add(p2)

    db.session.commit()

    # exibir a opiniao e a pessoa em postagem
    print(p2)

    # exibir a pessoa no format json
    print(p2.json())
