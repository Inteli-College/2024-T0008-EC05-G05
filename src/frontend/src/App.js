import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'; // Import Routes
import LoginForm from './pages/LoginForm/LoginForm';

import Dashboard from './pages/dashboard/dashboard.jsx';
import Supplies from './pages/supplies/supplies.js';
import KitCard from './components/kit_card/kit_card.jsx';
import Home from './pages/home/home.jsx'

function App() {
  return (
    <Router>
      <div>
        <Routes>
          <Route path='/home' element={<Home />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/supplies" element={<Supplies />} />
          <Route path='/api/get-kits' element={<KitCard />} />
          <Route path="/" element={<Login />} /> {/* Define a Home component for the login */}
        </Routes>
      </div>
    </Router>
  );
}

// Define a Home component to render when no specific route is matched
function Login() {
  return (
    <div>
      <LoginForm />
    </div>
  );
}

export default App;