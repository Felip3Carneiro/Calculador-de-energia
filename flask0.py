from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def comeco():
    return '''
    <head>
        <title>Minha Página Flask</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p><a href='/felipe_secret'>Clique aqui para descobrir quem é Felipe</a></p>
        <p><a href='/random_fact'>Clique aqui para descobrir um fato aleatório sobre Felipe</a></p>
        <p><a href='/jogo'>Cara ou Coroa</a></p>
        <p><a href='/geradordesenhas'>Gerador de Senhas</a></p>
    </body>
    '''


@app.route("/felipe_secret")
def felipe():
    nome = "Felipe"
    return f"<h1> 😭Quem é você? {nome}?</h1>"

@app.route("/random_fact")
def random_fact():
    facts = [
        "Felipe é um desenvolvedor de software.",
        "Felipe gosta de programar em Python.",
        "Felipe mora em Lorena."
    ]
    return f"<h1> Fato aleatório: {random.choice(facts)}</h1>"


@app.route("/jogo")
def jogo():
    resultado = random.choice(["Cara", "Coroa"])
    return f"<h1>Resultado: {resultado}</h1>"

@app.route("/geradordesenhas")
def gerar_senha():
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    senha = ''.join(random.choice(caracteres) for i in range(12))
    return f"<h1>Sua senha gerada é: {senha}</h1>"

app.run(debug=True)
