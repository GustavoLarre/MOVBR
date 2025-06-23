from flask import Flask, render_template, request
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["movbr"]

# 🔧 Cria coleções e índices automaticamente se ainda não existirem
def setup_collection(name, geo_fields=[]):
    if name not in db.list_collection_names():
        db.create_collection(name)
        print(f"✅ Criada coleção: {name}")
    for field in geo_fields:
        db[name].create_index([(field, "2dsphere")])
        print(f"🌍 Índice geoespacial criado em: {name}.{field}")

setup_collection("rotas", ["origem", "destino"])
setup_collection("paradas", ["localizacao"])
setup_collection("turismo", ["localizacao"])

@app.route("/")
def home():
    rotas = list(db.rotas.find())
    return render_template("home.html", rotas=rotas)

@app.route("/rota/<id>")
def rota_detalhe(id):
    rota = db.rotas.find_one({"_id": ObjectId(id)})
    return render_template("rota_detalhe.html", rota=rota)

@app.route("/paradas")
def paradas():
    paradas = list(db.paradas.find())
    return render_template("paradas.html", paradas=paradas)

@app.route("/paradas-proximas")
def paradas_proximas():
    paradas = list(db.paradas.find())
    return render_template("paradas_proximas.html", paradas=paradas)

@app.route("/turismo")
def pontos_turisticos():
    pontos = list(db.turismo.find())
    return render_template("pontos_turisticos.html", pontos=pontos)

if __name__ == "__main__":
    app.run(debug=True)
