#from crypt import methods
from config import *
from modelo import *

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def incluir_pessoa():
    if request.method == 'GET':
        return render_template("cadastro.html")
    else:
        resposta = jsonify({"resultado": "ok", "detalhes": "oi"})     
        dados = request.get_json(force = True)  # (force=True) dispensa Content-Type na requisição
        try:  
            nova = Pessoa(**dados) 
            db.session.add(nova) 
            db.session.commit()  
        except Exception as e:  # em caso de erro...
            resposta = jsonify({"resultado": "erro", "detalhes": str(e)})
        resposta.headers.add("Access-Control-Allow-Origin", "*")
        return resposta 

@app.route('/fazer_login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        dados = request.get_json(force=True)
        email = str(dados['email'])
        senha = str(dados['senha'])
        print(dados)

        resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta 
#teste_rota: curl -d '{"email":"josilva@gmail.com", "senha":"1234567"}' -X POST" localhost:5000/fazer_login

@app.route('/index', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

@app.route('/em_alta', methods = ['GET', 'POST'])
def em_alta():
    if request.method == 'GET':
        return render_template ('em_alta.html')

@app.route('/inicio', methods = ['GET', 'POST'])
def inicio():
    if request.method == 'GET':
        return render_template('inicio.html')

@app.route('/incluir_livro', methods = ['GET', 'POST'])
def incluir_livro():
    if request.method == 'GET':
        return render_template ('cadastro_livro.html')
def salvar_imagem():
    try:
        print("comecando")
        file_val = request.files['foto']
        print("vou salvar em: "+file_val.filename)
        print(path)
        arquivoimg = os.path.join(path, 'imagens/'+file_val.filename)
        file_val.save(arquivoimg)
        r = jsonify({"resultado":"ok", "detalhes": file_val.filename})
    except Exception as e:
        r = jsonify({"resultado":"erro", "detalhes": str(e)})

    r.headers.add("Access-Control-Allow-Origin", "*")
    return r

'''@app.route("/save_image", methods=['POST'])'''

@app.route('/get_image/<int:id>')
def get_image(id):
    livro = db.session.query(Pessoa).get(id_pessoa)
    arquivoimg = os.path.join(caminho, 'imagens/'+ livro.nome_foto)
    return send_file(arquivoimg, mimetype='image/gif')
       
app.run(debug=True, host='0.0.0.0', port=5000)