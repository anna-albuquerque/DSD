from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
@app.route('/api1', methods=['GET', 'POST'])

def api1():
    if request.method == 'POST':
        message = request.form['message']
        messages.append(message)
        return "Mensagem recebida na API 1: " + message
    else:
        return "<h1>API 1 está funcionando!</h1><br>Mensagens recebidas: " + ', '.join(messages)

if __name__ == '__main__':
    app.run(port=5001)