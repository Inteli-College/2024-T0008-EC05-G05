import React, { useState, useEffect, useCallback } from 'react';
import './log_atividades.css'

const mapPeriod = {
  dia: 'day',
  semana: 'week',
  mes: 'month',
  ano: 'year',
};

const FetchLogs = () => {
  const [logs, setLogs] = useState([]);
  const [timePeriod, setTimePeriod] = useState('dia'); // Default to 'dia'

  const fetchLogs = useCallback(async () => {
    const period = mapPeriod[timePeriod] || 'day';
    const url = `http://127.0.0.1:8000/log/logs/${period}`;

    try {
      const response = await fetch(url);
      const jsonData = await response.json();
      setLogs(jsonData);
      console.log("Logs fetched:", jsonData);
    } catch (error) {
      console.error('Failed to fetch logs:', error);
      setLogs([]); // Clear logs in case of an error
    }
  }, [timePeriod]);

  useEffect(() => {
    fetchLogs();
  }, [fetchLogs]);

  const handleTimePeriodChange = (event) => {
    setTimePeriod(event.target.value);
  };

  return (
    <div className="table-container">
      <div className="table-header">
        <div>
          <label htmlFor="log-period">Escolha um período: </label>
          <select id="log-period" value={timePeriod} onChange={handleTimePeriodChange}>
            <option value="dia">Dia</option>
            <option value="semana">Semana</option>
            <option value="mes">Mês</option>
            <option value="ano">Ano</option>
          </select>
        </div>
      </div>
      <div className="scrollable-table">
        <table>
          <thead>
            <tr>
              <th>Usuário</th>
              <th>Atividade</th>
              <th>Kit</th>
              <th>Horário</th>
              <th>Data</th>
            </tr>
          </thead>
          <tbody>
            {logs.map((item, index) => (
              <tr key={index}>
                <td>{item.user}</td>
                <td>{item.activity}</td>
                <td>{item.kit || 'N/A'}</td> {/* Assuming 'kit' might not be in the second return */}
                <td>{item.hour || 'N/A'}</td> {/* Assuming 'hour' might not be in the second return */}
                <td>{item.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
export default FetchLogs;