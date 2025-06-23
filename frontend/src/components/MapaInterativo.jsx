import React, { useEffect, useState } from "react";
import { MapContainer, TileLayer, Marker, Popup, useMap } from "react-leaflet";
import "leaflet/dist/leaflet.css";

// Corrige ícones do Leaflet
import L from "leaflet";
delete L.Icon.Default.prototype._getIconUrl;
L.Icon.Default.mergeOptions({
  iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
  iconUrl: require("leaflet/dist/images/marker-icon.png"),
  shadowUrl: require("leaflet/dist/images/marker-shadow.png"),
});

function MapaInterativo() {
  const [posicao, setPosicao] = useState(null);

  useEffect(() => {
    navigator.geolocation.getCurrentPosition(
      (pos) => {
        setPosicao([pos.coords.latitude, pos.coords.longitude]);
      },
      (erro) => {
        console.error("Erro ao obter localização:", erro);
        setPosicao([-15.78, -47.93]); // Fallback: Brasília
      }
    );
  }, []);

  if (!posicao) return <p>Localizando...</p>;

  return (
    <MapContainer center={posicao} zoom={14} style={{ height: "400px", width: "100%" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; OpenStreetMap contributors'
      />
      <Marker position={posicao}>
        <Popup>Você está aqui</Popup>
      </Marker>
    </MapContainer>
  );
}

export default MapaInterativo;
