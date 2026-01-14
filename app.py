from flask import Flask

app = Flask(__name__)
@app.router('/')
def hola():
    return "<h1>¡HOLA MARTHA I.A Integracion de sistemas y arquitectura!<h1>"

if __name__== '__main__':
    app.run(host="0.0.0.0", port=5000)
