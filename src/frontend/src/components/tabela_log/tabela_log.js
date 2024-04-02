import React, { useState, useEffect, useCallback } from 'react';
import './tabela_log.css';

const mapPeriod = {
  dia: 'day',
  semana: 'week',
  mes: 'month',
  ano: 'year',
};

const TabelaLog = ({ title }) => {
  const [data, setData] = useState([]);
  const [timePeriod, setTimePeriod] = useState('dia'); // Default to 'dia', aligned with dropdown values

  // Mapping to match internal state to the API's expected period parameters


  // Memoized fetchData function to fetch data from the API
  const fetchData = useCallback(async () => {
    console.log("Fetching data for", title, "with period", timePeriod);
    // Adjust the endpoint based on the title
    const endpoint = title.toLowerCase() === 'itens' ? '/log/itens' : '/log/kits';
    // Append the selected period to the URL
    const period = mapPeriod[timePeriod] || 'day';
    const url = `http://127.0.0.1:8000${endpoint}/${period}`;

    try {
      const response = await fetch(url);
      const jsonData = await response.json();
      setData(jsonData);
      console.log("Data fetched:", jsonData);
    } catch (error) {
      console.error('Failed to fetch data:', error);
      setData([]); // Clear data in case of an error
    }
  }, [title, timePeriod]); // Dependencies

  useEffect(() => {
    fetchData();
  }, [fetchData]); // Dependency array includes fetchData now

  const handleTimePeriodChange = (event) => {
    console.log("Time period selected:", event.target.value);
    setTimePeriod(event.target.value);
  };

  return (
    <div className="table-container">
      <div className="table-header">
        <h2>{title}</h2>
        <div>
          <label htmlFor="periodo">Escolha um período: </label>
          <select id="periodo" value={timePeriod} onChange={handleTimePeriodChange}>
            <option value="dia">Dia</option>
            <option value="semana">Semana</option>
            <option value="mes">Mes</option>
            <option value="ano">Ano</option>
          </select>
        </div>
      </div>

      <div className="scrollable-table">
        <table>
          <thead>
            <tr>
              <th>{title === 'Itens' ? 'Nome' : 'Número do Kit'}</th>
              <th>Quantidade</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{title === 'Itens' ? item.nome : item.numero_do_kit}</td>
                <td>{item.quantity}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TabelaLog;