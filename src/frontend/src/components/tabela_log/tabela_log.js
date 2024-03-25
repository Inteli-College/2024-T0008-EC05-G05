import React, { useState, useEffect } from 'react';
import './tabela_log.css';

const TabelaLog = ({ tableName, title }) => {
  const [timePeriod, setTimePeriod] = useState('dia'); // Default to 'dia'

  // Hard-coded data sets for each time period
  const dataSets = {
    dia: [
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
      { nome: 'Dia Item 1', quantidade: 1 },
      { nome: 'Dia Item 2', quantidade: 2 },
    ],
    semana: [
      { nome: 'Semana Item 1', quantidade: 3 },
      { nome: 'Semana Item 2', quantidade: 4 },
    ],
    mes: [
      { nome: 'Mes Item 1', quantidade: 5 },
      { nome: 'Mes Item 2', quantidade: 6 },
    ],
    ano: [
      { nome: 'Ano Item 1', quantidade: 7 },
      { nome: 'Ano Item 2', quantidade: 8 },
    ],
  };

  // Select the data set based on the current time period
  const data = dataSets[timePeriod];

  const handleTimePeriodChange = (event) => {
    setTimePeriod(event.target.value);
  };

  return (
    <div className="table-container">
      <h2>{title}</h2>
      {/* Dropdown for selecting the time period */}
      <div>
        <label htmlFor="periodo">Escolha um período: </label>
        <select id="periodo" value={timePeriod} onChange={handleTimePeriodChange}>
          <option value="dia">Dia</option>
          <option value="semana">Semana</option>
          <option value="mes">Mes</option>
          <option value="ano">Ano</option>
        </select>
      </div>
      {/* Render your table here */}
      <table>
        <thead>
          <tr>
            <th>nome</th>
            <th>quantidade</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, index) => (
            <tr key={index}>
              <td>{item.nome}</td>
              <td>{item.quantidade}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default TabelaLog;