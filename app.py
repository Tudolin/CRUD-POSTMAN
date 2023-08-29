# 1 - OBJETIVO - Api para notas de Filmes, estilo Letterbox, com inclusão, consulta, edição e exclusão
# 2 - URL BASE - localhost
# 3 - ENDPOINT (endereço que deve ser chamado para executar determinada função dentro da API) - localhost/filmes (GET), localhost/filmes (POST), localhost/livros/id (GET by ID), localhost/livros/id (PUT), localhost/livros/id (DELETE) 
# 4 - RECURSOS - Filmes e suas Notas

from flask import Flask, jsonify, request

app = Flask(__name__)

filmes = [
    {
        'id':1,
        'titulo': 'A viagem de Chihiro',
        'diretor': 'Hayao Miyazaki',
        'imdb': 8.6,
        'ano': 2001
    },
    {
        'id':2,
        'titulo': 'Django Livre',
        'diretor': 'Quentin Tarantino',
        'imdb': 8.5,
        'ano': 2012
    },
    {
        'id':3,
        'titulo': 'O Senhor dos Anéis: O Retorno do Rei',
        'diretor': 'Peter Jackson',
        'imdb': 9,
        'ano': 2003
    }
]


#INCLUIR FILME
@app.route('/filmes', methods=['POST'])
def include_filme():
    novo_filme = request.get_json()
    filmes.append(novo_filme)
    return jsonify(filmes)

#CONSULTAR A TODOS
@app.route('/filmes',methods=['GET'])
def get_movie():
    return jsonify(filmes)

#CONSULTAR POR ID
@app.route('/filmes/<int:id>',methods=['GET'])
def get_filme_byid(id):
    for filme in filmes:
        if filme.get('id') == id:
            return jsonify(filme)

#EDITAR
@app.route('/filmes/<int:id>', methods=['PUT'])
def edit_filme_byid(id):
    filme_changed = request.get_json()
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            filmes[indice].update(filme_changed)
            return jsonify(filmes[indice])

#EXCLUIR
@app.route('/filmes/<int:id>', methods=['DELETE'])
def excluir_filme_byid(id):
    for indice,filme in enumerate(filmes):
        if filme.get('id') == id:
            del filmes[indice]    
    return jsonify(filmes)

app.run(port=5000, host='localhost', debug=True)