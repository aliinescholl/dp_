from config import *

class Forum(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    opiniao = db.Column(db.String(254))
    nota = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str (self.nome + ", " + self.opiniao + ', ' + self.nota)
    # expressao da classe no formato json
    
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "opiniao": self.opiniao,
            'nota': self.nota
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Forum
    p1 = Forum(nome = "João da Silva", opiniao = "pessimo livro", nota = '5')

    # persistir
    db.session.add(p1)
    db.session.commit()
    
    # exibir a opiniao da pessoa
    print(p1)

    # exibir a pessoa no format json
    print(p1.json())