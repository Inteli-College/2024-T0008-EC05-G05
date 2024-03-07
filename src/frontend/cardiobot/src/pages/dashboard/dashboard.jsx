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
        <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
        <div className={sidebarOpen ? 'main-content blurred' : 'dashboard-content'}>
          <h1>Bem-vindo à Dashboard</h1>
        </div>
    </div>
  );
}

export default Dashboard;
