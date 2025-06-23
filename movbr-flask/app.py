from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_bcrypt import Bcrypt
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "senha123"  
app.permanent_session_lifetime = timedelta(days=7)

client = MongoClient("mongodb://localhost:27017/")
db = client["movbr"]
bcrypt = Bcrypt(app)

# 🔧 Cria coleções e índices
def setup_collection(name, geo_fields=[]):
    if name not in db.list_collection_names():
        db.create_collection(name)
    for field in geo_fields:
        db[name].create_index([(field, "2dsphere")])

setup_collection("rotas", ["origem", "destino"])
setup_collection("paradas", ["localizacao"])
setup_collection("turismo", ["localizacao"])
setup_collection("horarios")
setup_collection("usuarios")

# 🔄 Serializadores
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

# 🧑‍💻 Autenticação
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        senha = request.form["senha"]
        user = db.usuarios.find_one({"email": email})
        if user and bcrypt.check_password_hash(user["senha"], senha):
            session["usuario"] = user["nome"]
            return redirect(url_for("home"))
        flash("Credenciais inválidas", "danger")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("home"))

@app.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        senha = request.form["senha"]
        if db.usuarios.find_one({"email": email}):
            flash("Email já cadastrado", "warning")
            return redirect(url_for("registro"))
        senha_hash = bcrypt.generate_password_hash(senha).decode("utf-8")
        db.usuarios.insert_one({
            "nome": nome,
            "email": email,
            "senha": senha_hash
        })
        flash("Cadastro realizado com sucesso!", "success")
        return redirect(url_for("login"))
    return render_template("registro.html")

# 🔗 Rotas de API
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

# 🌐 Rotas Web
@app.route("/")
def home():
    rotas = list(db.rotas.find())
    return render_template("home.html", rotas=rotas, usuario=session.get("usuario"))

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
