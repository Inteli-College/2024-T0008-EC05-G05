import React, { useState } from 'react';
import './dashboard.css'; // Importa estilos para o componente Dashboard
import Sidebar from '../../components/Sidebar/Sidebar.js'; // Importa o componente Sidebar
import TabelaLog from '../../components/tabela_log/tabela_log.js'; // Importa o componente TabelaLog
import LogAtividades from '../../components/log_atividades/log_atividades.js'; // Importa o componente LogAtividades

function Dashboard() {
    const [sidebarOpen, setSidebarOpen] = useState(false); // Estado para controlar se a barra lateral está aberta ou fechada
    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen); // Função para alternar o estado da barra lateral entre aberta e fechada
    };

    return (
        <div className="dashboard">
            <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} /> {/* Renderiza o componente Sidebar passando props */}
            <div className="main-content">
                <div className="dashboard-header">
                    <h1 className="dashboard-title">Dashboard</h1>
                </div>
                <div className="tables-container">
                    <div className='tabela_kits'>
                        <TabelaLog tableName="tabela_kits" title="Kits" /> {/* Renderiza a tabela de kits */}
                    </div>
                    <div className='tabela_itens'>
                        <TabelaLog tableName="tabela_itens" title="Itens" /> {/* Renderiza a tabela de itens */}
                    </div>
                </div>
                <div className='log_atividades'>
                    <LogAtividades tableName="log_atividades" title="log" /> {/* Renderiza o log de atividades */}
                </div>
            </div>

        </div>
    );
}

export default Dashboard;

