import requests
from pymongo import MongoClient, GEOSPHERE
from datetime import datetime

OVERPASS_URL = "https://overpass-api.de/api/interpreter"

client = MongoClient("mongodb://localhost:27017/")
db = client["movbr"]
db.paradas.create_index([("localizacao", GEOSPHERE)])
db.turismo.create_index([("localizacao", GEOSPHERE)])

def consulta_overpass(query):
    print("🌐 Enviando consulta para Overpass...")
    r = requests.post(OVERPASS_URL, data={"data": query})
    r.raise_for_status()
    return r.json()

def importar_paradas():
    query_paradas = """
    [out:json][timeout:60];
    node["highway"="bus_stop"](area:3600061444);
    out body;
    """
    dados = consulta_overpass(query_paradas)
    novos = 0
    for el in dados.get("elements", []):
        if el["type"] != "node":
            continue
        doc = {
            "osm_id": el["id"],
            "nome": el.get("tags", {}).get("name", "Parada sem nome"),
            "localizacao": {
                "type": "Point",
                "coordinates": [el["lon"], el["lat"]]
            },
            "fonte": "OpenStreetMap",
            "tipo": "parada",
            "atualizado_em": datetime.utcnow()
        }
        res = db.paradas.update_one({"osm_id": el["id"]}, {"$set": doc}, upsert=True)
        if res.upserted_id:
            novos += 1
    print(f"🚌 Paradas importadas: {novos}")

def importar_pontos_turisticos():
    query_pontos = """
    [out:json][timeout:60];
    (
      node["tourism"~"museum|attraction|viewpoint|artwork|gallery|zoo"](area:3600061444);
      node["historic"](area:3600061444);
    );
    out body;
    """
    dados = consulta_overpass(query_pontos)
    novos = 0
    for el in dados.get("elements", []):
        if el["type"] != "node":
            continue
        tags = el.get("tags", {})
        doc = {
            "osm_id": el["id"],
            "nome": tags.get("name", "Ponto sem nome"),
            "descricao": tags.get("tourism") or tags.get("historic") or "ponto turístico",
            "localizacao": {
                "type": "Point",
                "coordinates": [el["lon"], el["lat"]]
            },
            "fonte": "OpenStreetMap",
            "tipo": "turismo",
            "atualizado_em": datetime.utcnow()
        }
        res = db.turismo.update_one({"osm_id": el["id"]}, {"$set": doc}, upsert=True)
        if res.upserted_id:
            novos += 1
    print(f"🏛️ Pontos turísticos importados: {novos}")

if __name__ == "__main__":
    print("🔁 Iniciando importação para Brasília...")
    importar_paradas()
    importar_pontos_turisticos()
    print("✅ Importação concluída.")
