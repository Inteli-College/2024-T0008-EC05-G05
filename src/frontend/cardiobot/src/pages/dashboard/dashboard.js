import React from 'react';
import './dashboard.css'; // Crie um arquivo de CSS para estilizações específicas desta página

import Sidebar from '../../components/Sidebar/Sidebar.js';

function Dashboard() {
  return (
    <div className="dashboard">
      <Sidebar />
      <div className="dashboard-content">
        {/* Todo o conteúdo da sua página Dashboard iria aqui */}
        <h1>Bem-vindo à Dashboard</h1>
        <Sidebar />
        {/* Você pode adicionar mais componentes aqui conforme necessário */}
      </div>
    </div>
  );
}

export default Dashboard;
