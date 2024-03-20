import React, { useState } from 'react';
import Sidebar from '../../components/Sidebar/Sidebar.js';

function Dashboard() {
    const [sidebarOpen, setSidebarOpen] = useState(false);
    const toggleSidebar = () => {
        setSidebarOpen(!sidebarOpen);
    };

    return (
        <div className="dashboard">
            <Sidebar open={sidebarOpen} toggleSidebar={toggleSidebar} />
            <div className={sidebarOpen ? "big-space" : 'small-space'}></div>

            <div className={sidebarOpen ? 'blurred' : 'banana'}>
                <h1>Bem-vindo à Dashboard</h1>
            </div>
        </div>
    )
}


export default Dashboard;