# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request, url_for

app = Flask(__name__)

livros = [
  {
    "id": 1,
    "titulo": "HTML 5 + CSS",
    "preco": 120,
    "bestseller": True
  },
  {
    "id": 2,
    "titulo": "JAVA PARA NERDS",
    "preco": 65,
    "bestseller": False
  },
  {
    "id": 3,
    "titulo": "PYTHON COM FLASK",
    "preco": 80,
    "bestseller": True
  },
  {
    "id": 4,
    "titulo": "ENGENHARIA DE SOFTWARE",
    "preco": 76,
    "bestseller": False
  },
  {
    "id": 5,
    "titulo": "ALGORITMOS",
    "preco": 54,
    "bestseller": False
  }
]
# funcionando
@app.route('/livraria/api/v1.0/livro', methods=['GET'])
def get_livros():
    return jsonify({'livros': livros})

# funcionando
@app.route('/livraria/api/v1.0/livro/<int:livro_id>', methods=['GET'])
def get_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        abort(404)
    return jsonify({'livro': livro[0]})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/livraria/api/v1.0/livro/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    livro = [livro for livro in livros if livro['id'] == livro_id]
    if len(livro) == 0:
        abort(404)
    else:
        
        livros.remove(livro[0])
        
        return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
