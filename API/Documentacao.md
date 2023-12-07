# Documentação da API Gateway
## Visão Geral

A API Gateway foi projetada para rotear solicitações para múltiplas APIs. Atualmente, ela suporta duas APIs: API1 e API2.

## Endpoint
O endpoint da API Gateway é ```/api_gateway```

## Métodos HTTP Suportados
A API Gateway suporta os seguintes métodos HTTP:
* ```GET```
* ```POST```

## Respostas
As respostas da API Gateway são retornadas como strings de texto.

## GET
Se uma solicitação GET for enviada para a API Gateway, ela retornará a string “API Gateway está funcionando!”.

## POST
Se uma solicitação POST for enviada para a API Gateway, ela encaminhará a mensagem para as APIs 1 e 2 e retornará as respostas concatenadas dessas APIs.

## Parâmetros
A API Gateway aceita os seguintes parâmetros na solicitação POST:
* ```message```: A mensagem de texto que será enviada para as APIs 1 e 2.
Exemplo de Uso
Para usar a API Gateway, você pode enviar uma solicitação POST para http://localhost:5000/api_gateway com o parâmetro "message" no corpo da solicitação.

Por favor, note que esta é uma documentação básica e pode precisar de ajustes para atender às suas necessidades específicas. Além disso, certifique-se de que a porta usada (5000) está disponível em seu sistema.

</br></br>

# Prepação do ambiente
Na pasta raiz da aplicação execute os seguintes comandos:
```
python -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install flask requests
```
## Execução do programa 
Abra um terminal para cada API
```
python gateway.py
python api1.py
python api2.py
```
Abra o navegador e verifique se as rotas das APIs estão funcionais, após verificar abra o arquivo cliente.html no  navegador.

## Encerramento do ambiente
```
deactivate
rm venv
```