from flask import Flask , render_template


TEMPLATES ='./template'
STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)
@app.route('/')
def olaMundo():
    return 'ola mundo'

@app.route('/index')
def index():
    nome= 'ewerton'
    mostrarVideos = True
    lista =['https://www.youtube.com/embed/d35pHYwgVpg','https://www.youtube.com/embed/VTSIrwHUZ-M']
    return render_template('index.html', nome = nome, lista = lista, mostrarVideos = mostrarVideos)

#app.run(host='0.0.0.0', port=5000)