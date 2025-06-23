import React from 'react';
import { Link } from 'react-router-dom';

<Link to={`/rota/${rota.id}`}>Ver detalhes</Link>


function Home() {
  return (
    <div>
      <h1>Bem-vindo ao MOVBR</h1>
      <p>Use o campo de busca para encontrar rotas de ônibus no DF.</p>
    </div>
  );
}

export default Home;
