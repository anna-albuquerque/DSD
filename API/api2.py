from flask import Flask, request

app = Flask(__name__)

messages = []

@app.route('/', methods=['GET'])
@app.route('/api2', methods=['GET', 'POST'])
def api2():
    if request.method == 'POST':
        message = request.form['message']
        messages.append(message)
        return "Mensagem recebida na API 2: " + message
    else:
        return "<h1>API 2 está funcionando!</h1><br>Mensagens recebidas: " + ', '.join(messages)

if __name__ == '__main__':
    app.run(port=5002)