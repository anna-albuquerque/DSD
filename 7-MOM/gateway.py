from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/publicar', methods=['POST'])
def publicar():
    mensagem = request.json['mensagem']
    requests.post('http://localhost:5001/publicar', json={'mensagem': mensagem})
    return jsonify({'status': 'Mensagem publicada com sucesso!'})

@app.route('/consumir', methods=['GET'])
def consumir():
    response = requests.get('http://localhost:5002/consumir')
    return jsonify({'mensagens': response.json()})

if __name__ == '__main__':
    app.run(port=5000)