import React, { useState } from 'react';
import './dashboard.css';
import Sidebar from '../../components/Sidebar/Sidebar.js';
import TabelaLog from '../../components/tabela_log/tabela_log.js';
import LogAtividades from '../../components/log_atividades/log_atividades.js';

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
                        <TabelaLog tableName="tabela_kits" title="Kits" />
                    </div>
                    <div className='tabela_itens'>
                        <TabelaLog tableName="tabela_itens" title="Itens" />
                    </div>
                </div>
                <div className='log_atividades'>
                    <LogAtividades tableName="log_atividades" title="log" />
                </div>
            </div>

        </div>
    );
}

export default Dashboard;
