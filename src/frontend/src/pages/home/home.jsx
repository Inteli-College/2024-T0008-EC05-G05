import React, { useState } from 'react';
import './home.css'; // Crie um arquivo de CSS para estilizações específicas desta página
import { FaBars } from "react-icons/fa"; // Ícone de menu (hambúrguer)
import Sidebar from '../../components/Sidebar/Sidebar.js';
import KitCard from '../../components/kit_card/kit_card.jsx';
import KitsProdStatus from '../../components/KitsProd/KitsProdStatus.js';
import logo from '../../assets/imgs/logo-grupo.svg';

function Home() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const toggleSidebar = () => {
    setSidebarOpen(!sidebarOpen);
  };

  const kitsInfo = [
    {
      name: 'Kit 1',
      image: 'https://via.placeholder.com/150',
      startTime: '03/11/2024 14:30:00',
    },
    {
      name: 'Kit 2',
      image: 'https://via.placeholder.com/150',
      startTime: '03/11/2024 14:30:00',
    },
    {
      name: 'Kit 3',
      image: 'https://via.placeholder.com/150',
      startTime: '03/11/2024 14:30:00',
    },
  ];


  return (
    <div className="home">
        <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
        <div className={sidebarOpen ? "big-space" : 'small-space'}></div>
        <div className='header'>
          <h2 className='kit-card-title'>Página Inicial</h2>
          <div className='header-logo'><h2>Cardio-Bot</h2><img src={logo}  alt="logo"></img></div>
        </div>
        <div className='page-content'>
          <KitCard />
          <div className="production-kits-section">
            <h2>Kits em produção  </h2>
            {kitsInfo.map((kit, index) => (
              <KitsProdStatus 
                kitName={kit.name}
                imageUrl={kit.image}
                startTime={kit.startTime}
                isFirst={index === 0}
              />
            ))}
          </div>
        </div>
    </div>
  );
}
export default Home;
