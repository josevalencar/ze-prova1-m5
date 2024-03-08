# app.py
from flask import Flask, render_template, request, redirect, url_for
from tinydb import TinyDB
import json

app = Flask(__name__)

db = TinyDB("caminhos.json")

def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return json.load(arquivo)


@app.route("/novo")
def index():
    return render_template("index.html")

@app.route("/listas_caminhos", methods=["GET", "POST"])
def sobre(nome=None):
    if request.method == "POST":
        nome = request.form.get("nome")
        db.insert({"nome": nome})
    posts = db.all()
    return render_template("sobre.html", nome=nome, posts=posts)

@app.route("/pegar_caminho/<nome>")
def pegar_caminho(nome):
    dados_lidos = ler_arquivo('caminhos.json')
    ponto = dados_lidos['_default'][nome]["nome"]
    print(ponto)
    return render_template("pegar_caminho.html", nome=nome, ponto=ponto)

@app.route("/atualizar/<nome>")
def atualizar_caminho(nome):
    dados_lidos = ler_arquivo('caminhos.json')
    ponto = dados_lidos['_default'][nome]["nome"]
    print(ponto)
    return render_template("atualizar.html", nome=nome, ponto=ponto)

@app.route("/atualizar", methods=["GET", "POST"])
def atualizar(nome=None):
    if request.method == "POST":
        dados_lidos = ler_arquivo('caminhos.json')
        ponto = dados_lidos['_default'][nome]["nome"]
        nome = request.form.get("nome")
        db.insert({ponto: nome})
    posts = db.all()
    return render_template("sobre.html")


@app.route("/deletar/<nome>")
def deletar_caminho(nome):
    return render_template("deletar.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)