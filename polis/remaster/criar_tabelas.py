from config import *
from modelo import *

if os.path.exists(arquivobd):
    os.remove(arquivobd)
'''
db.create_all()

if os.path.exists(arquivobdlivro):
    os.remove(arquivobdlivro)
'''
db.create_all()

print("Banco de dados e tabelas criadas")