// src/pages/Rota.jsx
import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { buscarRotaPorId } from '../services/api';
import { MapContainer, TileLayer, Marker, Polyline } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

export default function Rota() {
  const { id } = useParams();
  const [rota, setRota] = useState(null);

  useEffect(() => {
    async function carregarRota() {
      const dados = await buscarRotaPorId(id);
      setRota(dados);
    }
    carregarRota();
  }, [id]);

  if (!rota) return <p>Carregando...</p>;

  const origem = rota.origem.coordinates;
  const destino = rota.destino.coordinates;

  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold mb-2">{rota.nome}</h1>
      <p className="mb-4">{rota.descricao}</p>

      <MapContainer center={origem} zoom={13} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />
        <Marker position={origem} />
        <Marker position={destino} />
        <Polyline positions={[origem, destino]} color="blue" />
      </MapContainer>
    </div>
  );
}
