from config import *

#dados que serao recebidos e arquivados no cadastro
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    email = db.Column(db.String(254))
    senha = db.Column(db.String(254))

    def __str__(self):
        s = f"{self.id}, {self.nome}, {self.email}, {self.senha}"
        return s

    def json(self):
        return{
            "id":self.id, 
            "nome":self.nome, 
            "email":self.email,
            "senha":self.senha
        }
#teste de funcionamento
if __name__=="__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    #criar
    db.create_all()

    p1 = Usuario(nome = "aliinescholl", email = "email@gmail.com", senha = "123456")
#adicionar no banco de dados
    db.session.add(p1)
    db.session.commit()

    print(p1)
    print(p1.json())