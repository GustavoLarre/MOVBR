# MOVBR

🚍 MOVBR é uma aplicação web para facilitar o uso do transporte público no Distrito Federal, oferecendo visualização de rotas, paradas, horários e pontos turísticos diretamente em mapas interativos.

---

## 🗺️ Funcionalidades

- 🔍 Pesquisa de rotas por nome e visualização de detalhes.
- 🚌 Visualização de paradas e seus horários previstos.
- 🗺️ Mapas interativos com marcadores personalizados (Leaflet).
- 📍 Localização de paradas próximas com base na geolocalização do usuário.
- 🗿 Exibição de pontos turísticos próximos às paradas.
- 📲 Interface web responsiva baseada em templates HTML + CSS.
- ⚡ API RESTful com dados georreferenciados via MongoDB.

---

## 🏗️ Arquitetura

- 🔙 Backend: Flask + PyMongo
- 🌐 Frontend: HTML + CSS + JavaScript + Jinja2
- 💃 Banco de Dados: MongoDB com suporte a geolocalização (2dsphere)
- 🗺️ Integração: Leaflet.js para mapas + localização via navegador
- ⚙️ Organização: Rotas divididas por interface (HTML) e API (JSON)

---

## 🧠 Tecnologias Utilizadas

- Python 3.10+
- Flask
- PyMongo
- MongoDB
- Jinja2
- Leaflet.js
- HTML5 / CSS3
- JavaScript
- Geolocalização via navegador

---

## 📄 Modelagem de Dados (MongoDB)

As principais coleções usadas no banco movbr:

- rotas: { nome, descricao, origem, destino }
- paradas: { nome, localizacao (GeoJSON Point) }
- horarios: { parada (ObjectId), horario\_previsto }
- turismo: { nome, descricao, localizacao }

Todos os campos de geolocalização usam índice 2dsphere para permitir filtros por proximidade.

---

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos

- Python 3.10+
- MongoDB instalado e rodando localmente
- (Opcional) MongoDB Compass para gerenciar dados visualmente

### ▶️ Executando o app Flask

1. Clone o projeto:

```bash
git clone https://github.com/seuusuario/movbr.git
cd movbr
```

2. Crie o ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

3. Inicie o MongoDB local:

No terminal:

```bash
mkdir C:\data\db        # somente no Windows
mongod
```

4. Rode a aplicação:

```bash
python app.py
```

Acesse no navegador:

- [http://localhost:5000](http://localhost:5000) → site com mapas
- [http://localhost:5000/api/paradas](http://localhost:5000/api/paradas) → dados JSON da API

---

## 🧰 Testes e Debug

Como o app é leve, os testes iniciais podem ser feitos acessando os endpoints API diretamente no navegador ou Postman:

- /api/paradas
- /api/rotas
- /api/rotas/
- /api/turismo

Testes automatizados podem ser adicionados com pytest ou unittest futuramente.

---

## 💾 Dados de Exemplo

Os dados podem ser adicionados manualmente pelo MongoDB Compass nas coleções:

- rotas
- paradas
- horarios
- turismo

Ou criados com scripts Python (init\_mongo.py).

---

## 📁 Estrutura do Projeto

- app.py → principal servidor Flask
- templates/ → arquivos HTML (Jinja2)
- static/ → CSS, JS e ícones personalizados
- requirements.txt → dependências Python
- README.md → este guia

---

## 👥 Contribuidores

- Gabriel Kalebe
- Equipe MOVBR

---

## 📄 Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

