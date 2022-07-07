from configs.config import *

class Livrinho(db.Model):
    # atributos da pessoa
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(254))
    descricao = db.Column(db.String(254))
    autor = db.Column(db.String(254))

    # método para expressar a pessoa em forma de texto
    def __str__(self):
        return str(self.id)+") "+ self.titulo + ", " +\
            self.descricao + ", " + self.autor
    # expressao da classe no formato json
    def json(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descricao": self.descricao,
            "autor": self.autor
        }

# teste    
if __name__ == "__main__":
    # apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    l1 = Livrinho(titulo = "Harry Potter e a Pedra Filosofal", descricao = "Menino que ama fumar uma pedra", 
        autor = "J.K. Rowling")
    l2 = Livrinho(titulo = "Vermelho, branco e sangue azul", descricao = "Fanficona", 
        autor = "Casey McQuiston")        
    
    # persistir
    db.session.add(l1)
    db.session.add(l2)
    db.session.commit()
    
    # exibir a pessoa
    print(l2)

    # exibir a pessoa no format json
    print(l2.json())