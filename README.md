# MOVBR

🚍 **MOVBR** é uma aplicação web desenvolvida para otimizar e agilizar a experiência de uso do transporte público no Distrito Federal. A plataforma oferece geração de rotas inteligentes, monitoramento de veículos em tempo real e informações turísticas integradas.

---

## 🗺️ Funcionalidades

- 🔍 Pesquisa de rotas entre origem e destino.
- 🚌 Visualização da localização dos veículos em tempo real.
- 🗺️ Geração de itinerários com múltiplos modais.
- ⌛ Previsão de chegada dos ônibus às paradas.
- 🚨 Alertas sobre atrasos, mudanças de rota e interrupções.
- 🏞️ Exibição de pontos turísticos próximos às paradas.
- 🎯 Sugestões de passeios com base na localização atual.
- 🗺️ Mapas interativos com informações em camadas.

---

## 🏗️ Arquitetura

- **Backend:** Django + Django REST Framework (API RESTful).
- **Frontend:** React (Web responsiva).
- **Banco de Dados:** PostgreSQL com suporte a geolocalização via PostGIS.
- **Processamento Assíncrono:** Celery + Redis.
- **Containerização:** Docker.
- **Integrações:** APIs públicas de transporte, turismo e mapas.

---

## 🧠 Tecnologias Utilizadas

- Python 3.10+
- Django
- Django REST Framework
- ReactJS
- PostgreSQL + PostGIS
- Celery
- Redis
- Docker
- GeoPandas, GeoPy (para dados geoespaciais)
- APIs públicas (GTFS, OpenStreetMap, dados turísticos)

---

## 🗄️ Modelagem de Dados

**Principais Entidades:**

- `usuario`
- `veiculo`
- `rota`
- `parada`
- `itinerario`
- `itinerario_parada`
- `veiculo_rota`
- `ponto_turistico`
- `notificacao`

Com suporte geoespacial via campos `GEOGRAPHY(POINT, 4326)` nas tabelas relevantes.

---

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos

- Docker e Docker Compose instalados  
ou  
- Python 3.10+, Node.js, PostgreSQL com PostGIS manualmente.

### 📦 Executando com Docker (Recomendado)

```bash
git clone https://github.com/seuusuario/movbr.git
cd movbr
docker-compose up --build
```

Acesse no navegador:  
`http://localhost:3000` → Frontend  
`http://localhost:8000/api` → Backend API

### ⚙️ Executando manualmente

1. Configure o banco PostgreSQL com PostGIS.  
2. Backend (Django):

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

3. Frontend (React):

```bash
cd frontend
npm install
npm start
```

---

## 🗺️ Banco de Dados

Ativar extensão PostGIS no banco:

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

---

## 🧪 Testes

- Testes backend:

```bash
python manage.py test
```

- Testes frontend:

```bash
npm test
```

---

## 👥 Contribuidores

-  
- Equipe MOVBR

---

## 📄 Licença

Este projeto está sob licença (). Veja o arquivo [LICENSE](https://github.com/GustavoLarre/MOVBR/blob/2e62430176d4ea97f36220671e1713c5826f278e/LICENSE.txt) para mais detalhes.
