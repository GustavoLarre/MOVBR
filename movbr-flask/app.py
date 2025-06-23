from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId

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
setup_collection("horarios")  # agora inclui horários também

# Utilitários para serialização

def serialize_parada(parada):
    parada["_id"] = str(parada["_id"])
    parada["localizacao"] = parada.get("localizacao", {})
    horarios = list(db.horarios.find({"parada": parada["_id"]}))
    parada["horarios"] = [{"horario_previsto": str(h["horario_previsto"])} for h in horarios]
    return parada

def serialize_rota(rota):
    rota["_id"] = str(rota["_id"])
    rota["origem"] = rota.get("origem", {})
    rota["destino"] = rota.get("destino", {})
    return rota

def serialize_ponto(ponto):
    ponto["_id"] = str(ponto["_id"])
    ponto["localizacao"] = ponto.get("localizacao", {})
    return ponto

# 🔗 Rotas de API (JSON)

@app.route("/api/paradas")
def api_paradas():
    paradas = list(db.paradas.find())
    return jsonify([serialize_parada(p) for p in paradas])

@app.route("/api/rotas")
def api_rotas():
    rotas = list(db.rotas.find())
    return jsonify([serialize_rota(r) for r in rotas])

@app.route("/api/rotas/<id>")
def api_rota_detalhe(id):
    rota = db.rotas.find_one({"_id": ObjectId(id)})
    if not rota:
        return jsonify({"erro": "Rota não encontrada"}), 404
    return jsonify(serialize_rota(rota))

@app.route("/api/turismo")
def api_turismo():
    pontos = list(db.turismo.find())
    return jsonify([serialize_ponto(p) for p in pontos])

# 🌐 Rotas HTML (render_template)

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
    for p in paradas:
        p["horarios"] = list(db.horarios.find({"parada": p["_id"]}))
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
