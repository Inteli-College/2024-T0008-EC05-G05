import React, { useState, useEffect } from 'react';
import './log_atividades.css'


const Log_atividades = ({ tableName, title }) => {
    const [timePeriod, setTimePeriod] = useState('dia'); // Default to 'dia'
  
    // Updated data sets to include the "kit" property for each log entry
    const logDataSets = {
      dia: [
        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },
        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },        { user: 'User1', activity: 'Create', kit: 1, hour: '10:00', date: '25/03/2024' },
        { user: 'User2', activity: 'Delete', kit: 2, hour: '11:00', date: '25/03/2024' },
        { user: 'User3', activity: 'Update', kit: 3, hour: '12:00', date: '25/03/2024' },
    ],
      semana: [
        { user: 'User1', activity: 'Update', kit: 4, hour: '09:00', date: '20/03/2024' },
        { user: 'User2', activity: 'Create', kit: 5, hour: '10:00', date: '21/03/2024' },
      ],
      mes: [
        { user: 'User1', activity: 'Delete', kit: 1, hour: '15:00', date: '15/03/2024' },
        { user: 'User2', activity: 'Update', kit: 2, hour: '16:00', date: '10/03/2024' },
      ],
      ano: [
        { user: 'User1', activity: 'Create', kit: 3, hour: '13:00', date: '01/01/2024' },
        { user: 'User2', activity: 'Delete', kit: 4, hour: '14:00', date: '01/02/2024' },
      ],
    };
  
    // Select the log data set based on the current time period
    const data = logDataSets[timePeriod];
  
    const handleTimePeriodChange = (event) => {
      setTimePeriod(event.target.value);
    };
  
    return (
      <div className="table-container">
        <div className="table-header">
          <h2>{title}</h2>
          <div>
            <label htmlFor="log-period">Escolha um período: </label>
            <select id="log-period" value={timePeriod} onChange={handleTimePeriodChange}>
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
                <th>Usuário</th>
                <th>Atividade</th>
                <th>Kit</th> {/* New column header for Kit */}
                <th>Horário</th>
                <th>Data</th>
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  <td>{item.user}</td>
                  <td>{item.activity}</td>
                  <td>{item.kit}</td> {/* New column data for Kit */}
                  <td>{item.hour}</td>
                  <td>{item.date}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    );
  };
  
  export default Log_atividades;