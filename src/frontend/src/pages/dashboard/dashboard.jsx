import React, { useState } from 'react';
import './dashboard.css';
import Sidebar from '../../components/Sidebar/Sidebar.js';
import Tabela_log from '../../components/tabela_log/tabela_log.js';

function Dashboard() {
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };

    return (
        <div className="dashboard">
            <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
            <div className="main-content">
                <div className="dashboard-header">
                    <h1 className="dashboard-title">Dashboard</h1>
                </div>
                <div className="tables-container">
                    <div className='tabela_kits'>
                        <Tabela_log tableName="tabela_kits" title="Kits" />
                    </div>
                    <div className='tabela_items'>
                        <Tabela_log tableName="tabela_items" title="Items" />
                    </div>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;
