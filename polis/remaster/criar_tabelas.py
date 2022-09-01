from config import *
from modelo import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)

db.create_all()

print("Banco de dados e tabelas criadas")