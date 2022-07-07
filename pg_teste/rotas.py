from configs.config import *
from postagem.backend import *
from cadastro_livro.backend import *
from cadastro_pessoas.backend import *
from login_adm.login import *

@app.route("/")
def inicio():
    return 'backend operante, operação de editar'

app.run(debug=True)