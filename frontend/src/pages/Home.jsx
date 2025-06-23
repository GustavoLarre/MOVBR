import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div className="p-4">
      <h1>Bem-vindo ao MOVBR</h1>
      <p>Use o campo de busca para encontrar rotas de ônibus no DF.</p>

      <div className="mt-6">
        {rotas.map((rota) => (
          <div key={rota.id} className="border p-4 mb-4">
            <h2 className="text-xl font-bold">{rota.nome}</h2>
            <p>{rota.descricao}</p>
            <Link to={`/rota/${rota.id}`} className="text-blue-600 underline">
              Ver detalhes
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Home;
