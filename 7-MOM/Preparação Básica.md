## Prepação do ambiente 
Execute na pasta raiz da aplicação
```
python -m venv venv
.\venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install pika flask  
pip install websockets
choco install rabbitmq
```

## Execução do programa 
Abra um terminal para cada arquivo e digite:
```
python publisher.py
python subscriber.py
python gatreway.py
```
Abra o navegador e abra o arquivo client.html no navegador

## Encerramento do ambiente
```
deactivate
```