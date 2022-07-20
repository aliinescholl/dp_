from configs.config import *

from cadastro_livro.modelo import *
from cadastro_pessoas.modelo import *
from postagem.modelo import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)

db.create_all()

print("Banco de dados e tabelas criadas")
