import React, {useState} from 'react';
import './dashboard.css'; // Crie um arquivo de CSS para estilizações específicas desta página
import { FaBars } from "react-icons/fa"; // Ícone de menu (hambúrguer)

import Sidebar from '../../components/Sidebar/Sidebar.js';

function Dashboard() {
  const [sidebarOpen, setSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };
  
  return (
    <div className="dashboard">
      <FaBars className="menu-icon" onClick={toggleSidebar} />
      <main className={sidebarOpen ? 'main-content expanded' : 'main-content'}>
        <Sidebar open={sidebarOpen} />
        <div className="dashboard-content">
          {/* Todo o conteúdo da sua página Dashboard deve ser colocado aqui */}
          <h1>Bem-vindo à Dashboard</h1>
          {/* Você pode adicionar mais componentes aqui conforme necessário */}
        </div>
      </main>
    </div>
  );
}

export default Dashboard;
