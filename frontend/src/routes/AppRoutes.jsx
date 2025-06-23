import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Rota from '../pages/Rota';
import MapaParadas from '../pages/MapaParadas';
import MapaParadasComFiltro from '../pages/MapaParadasComFiltro';

function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/rota/:id' element={<Rota />} />
        <Route path='/paradas' element={<MapaParadas />} />
        <Route path='/paradas-proximas' element={<MapaParadasComFiltro />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
