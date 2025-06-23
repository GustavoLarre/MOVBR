export async function buscarRotas(busca) {
  try {
    const res = await fetch(`/api/rotas/?busca=${encodeURIComponent(busca)}`);
    return await res.json();
  } catch (err) {
    console.error('Erro ao buscar rotas:', err);
    return [];
  }
}

export async function buscarRotaPorId(id) {
  try {
    const res = await fetch(`/api/rotas/${id}/`);
    return await res.json();
  } catch (err) {
    console.error('Erro ao buscar rota:', err);
    return null;
  }
}

export async function buscarParadas() {
  try {
    const res = await fetch("http://localhost:8000/api/paradas/");
    return await res.json();
  } catch (err) {
    console.error("Erro ao buscar paradas:", err);
    return [];
  }
}

