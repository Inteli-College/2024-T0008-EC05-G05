import React, {useState} from 'react';
import './dashboard.css'; // Crie um arquivo de CSS para estilizações específicas desta página
import { FaBars } from "react-icons/fa"; // Ícone de menu (hambúrguer)
import Sidebar from '../../components/Sidebar/Sidebar.js';
import KitCard from '../../components/kit_card/kit_card.jsx';


function Dashboard() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };
  return (
    <div className="dashboard">
        <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
        <div className={sidebarOpen ? "big-space" : 'small-space'}></div>
        <section className='kit-card-section'>
          <h2 className='kit-car-title'> Kits </h2>
        </section>
        
        <div className={sidebarOpen ? 'blurred' : 'banana'}>
          <h1>Bem-vindo à Dashboard</h1>
        </div>
    </div>
  );
}
export default Dashboard;