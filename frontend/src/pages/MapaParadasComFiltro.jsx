import React, { useEffect, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import paradaIconImg from '../assets/bus-stop.png';
import { buscarParadas } from '../services/api';

const ParadaIcon = new L.Icon({
  iconUrl: paradaIconImg,
  iconSize: [30, 30],
  iconAnchor: [15, 30],
  popupAnchor: [0, -30],
});

function MapaParadasComFiltro() {
  const [paradas, setParadas] = useState([]);
  const [usuarioPos, setUsuarioPos] = useState(null);
  const [paradasProximas, setParadasProximas] = useState([]);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        setUsuarioPos([pos.coords.latitude, pos.coords.longitude]);
      },
      (err) => {
        console.error("Erro ao obter geolocalização:", err);
        setUsuarioPos([-15.78, -47.93]); 
      }
    );
  }, []);

  useEffect(() => {
    async function filtrarParadas() {
      const todas = await buscarParadas();
      if (!usuarioPos) return;

      const proximas = todas.filter((p) => {
        const [lng, lat] = p.localizacao.coordinates;
        const distancia = getDistanciaKm(usuarioPos, [lat, lng]);
        return distancia <= 1.0; // até 1 km
      });

      setParadasProximas(proximas);
      setParadas(todas);
    }

    filtrarParadas();
  }, [usuarioPos]);

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Paradas próximas (até 1 km)</h1>

      {usuarioPos && (
        <MapContainer center={usuarioPos} zoom={15} style={{ height: '500px', width: '100%' }}>
          <TileLayer
            url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            attribution="&copy; OpenStreetMap contributors"
          />

          <Marker position={usuarioPos}>
            <Popup>Sua localização</Popup>
          </Marker>

          {paradasProximas.map((parada) => (
            <Marker
              key={parada.id}
              position={parada.localizacao.coordinates.slice().reverse()}
              icon={ParadaIcon}
            >
              <Popup>
                <strong>{parada.nome}</strong><br />
                {parada.horarios.length > 0 ? (
                  <ul>
                    {parada.horarios.map((h, i) => (
                      <li key={i}>{h.horario_previsto}</li>
                    ))}
                  </ul>
                ) : (
                  <em>Sem horários disponíveis</em>
                )}
              </Popup>
            </Marker>
          ))}
        </MapContainer>
      )}
    </div>
  );
}

function getDistanciaKm(coord1, coord2) {
  const toRad = (value) => (value * Math.PI) / 180;
  const [lat1, lon1] = coord1;
  const [lat2, lon2] = coord2;

  const R = 6371; // km
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) *
    Math.sin(dLon / 2) * Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

export default MapaParadasComFiltro;
