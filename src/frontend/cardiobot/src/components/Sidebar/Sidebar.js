// Sidebar.js
import React from 'react';
import './Sidebar.css'; // Importe o CSS para estilização
import { CiMedicalCase } from "react-icons/ci";

function Sidebar() {
  return (
    <div className="sidebar">
      <div className="sidebar-menu">
        <div className="menu-item">
          <span className="icon"><CiMedicalCase /></span>
          <span className="title">Kits</span>
        </div>
        <div className="menu-item">
          <span className="icon">🔨</span>
          <span className="title">Estoque</span>
        </div>
        <div className="menu-item">
          <span className="icon">⚙️</span>
          <span className="title">Configurações do robô</span>
        </div>
        <div className="menu-item">
          <span className="icon">📈</span>
          <span className="title">Gestão</span>
        </div>
      </div>
    </div>
  );
}

export default Sidebar;
