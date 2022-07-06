from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estoque')
def estoque():
  arquivo = open("static/dataset.json")
  data = json.load(arquivo)
  return render_template('estoque.html', data=data)

@app.route('/comentarios')
def comentarios():
  arquivo = open("static/comments.json")
  cmnts = json.load(arquivo)
  return render_template('comentarios.html', comentarios=cmnts)

app.run(host='0.0.0.0', port=81)