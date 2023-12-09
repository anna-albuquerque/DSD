from flask import Flask, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    return "<h1>API Gateway está funcionando!</h1>"

@app.route('/api_gateway', methods=['GET', 'POST'])
def api_gateway():
    if request.method == 'POST':
        message = request.form['message']
        response1 = requests.get('https://api.thedogapi.com/v1/images/search')
        response2 = requests.post('http://localhost:5002/api2', data={'message': message})
        return response1.text + "\n" + response2.text
    else:
        return "<h1>API Gateway está funcionando!</h1>"

if __name__ == '__main__':
    app.run(port=5000)
