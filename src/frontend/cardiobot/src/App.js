import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'; // Import Routes

import Dashboard from './pages/dashboard/dashboard.js';
import Supplies from './pages/supplies/supplies.js';
import DataComponent from './pages/api/positions_catcher.js';
import KitCard from './components/kit_card/kit_card.js';

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/supplies" element={<Supplies />} />
          <Route path='/api/get-itens' element={<KitCard />} />
          <Route path='/api/get-positions' element = {<DataComponent/>} />
          <Route path="/" element={<Home />} /> {/* Define a Home component for the homepage */}
        </Routes>
      </div>
    </Router>
  );
}

// Define a Home component to render when no specific route is matched
function Home() {
  return (
    <div>
      <nav>
      <h1>Bem vindo a página inicial</h1>
        <ul>
          <li>
            <Link to="/dashboard">Dashboard</Link>
          </li>
          <li>
            <Link to="/supplies">Supplies</Link>
          </li>
          <li>
            <Link to="/api/get-positions">Table</Link>
          </li>
          <li>
            <Link to="/api/get-itens">Itens</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default App;