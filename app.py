from flask import Flask , render_template


TEMPLATE ='./template'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC)


@app.route('/')
def index():
    nome= 'ewerton'
    lista =['https://www.youtube.com/embed/d35pHYwgVpg','https://www.youtube.com/embed/VTSIrwHUZ-M']
    return render_template('index.html', nomeHtml = nome, lista = lista)

#app.run(host='0.0.0.0', port=5000)