// Sidebar.js
import React from 'react';
import './Sidebar.css'; // Importe o CSS para estilização
import { CiMedicalCase, CiBoxes} from "react-icons/ci";
import { GoGear } from "react-icons/go";
import { TfiDashboard } from "react-icons/tfi";
import { FaBars } from "react-icons/fa"; // Ícone de menu (hambúrguer)

function Sidebar({ open }) {

  return (
    <div className={open ? 'sidebar open' : 'sidebar'}>
      <div className="sidebar">
        <div className="sidebar-menu">
          <div className="menu-item">
            <span className="icon"><CiMedicalCase /></span>
            <span className="title">Kits</span>
          </div>
          <div className="menu-item">
            <span className="icon"><CiBoxes /></span>
            <span className="title">Estoque</span>
          </div>
          <div className="menu-item">
            <span className="icon"><GoGear /></span>
            <span className="title">Configurações do robô</span>
          </div>
          <div className="menu-item">
            <span className="icon"><TfiDashboard /></span>
            <span className="title">Gestão</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Sidebar;
