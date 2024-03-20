// Sidebar.js
import React, { useState } from 'react';
import './Sidebar.css'; // Importe o CSS para estilização
import { CiMedicalCase, CiBoxes } from "react-icons/ci";
import { GoGear } from "react-icons/go";
import { TfiDashboard } from "react-icons/tfi";
import { FaBars } from "react-icons/fa"; // Ícone de menu (hambúrguer)
import { NavLink } from 'react-router-dom';

function Sidebar({ open, toggleSidebar }) {

  return (
    <>
      <div className={open ? "sidebar open" : "sidebar"}>
        <FaBars className="toggle-menu-icon" onClick={toggleSidebar} />
        <div className="sidebar-menu">
          <NavLink to="/home" className="menu-item" activeClassName="active">
            <span className="icon"><CiMedicalCase /></span>
            <span className={open ? "menu-title" : "menu-title hidden"}>Home</span>
          </NavLink>
          <NavLink to="/supplies" className="menu-item" activeClassName="active">
            <span className="icon"><CiBoxes /></span>
            <span className={open ? "menu-title" : "menu-title hidden"}>Estoque</span>
          </NavLink>
          <NavLink to="/dashboard" className="menu-item" activeClassName="active">
            <span className="icon"><TfiDashboard /></span>
            <span className={open ? "menu-title" : "menu-title hidden"}>Dashboard</span>
          </NavLink>
        </div>
      </div>
      {open && <div className="sidebar-overlay" onClick={toggleSidebar}></div>}
    </>
  );
}

export default Sidebar;