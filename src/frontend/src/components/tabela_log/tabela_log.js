import React, { useState, useEffect } from 'react';
import './tabela_log.css';

const TabelaLog = ({ title }) => {
  const [data, setData] = useState([]);
  const [timePeriod, setTimePeriod] = useState('dia'); // Default to 'dia'

  // Função para buscar dados da API
  const fetchData = async () => {
    const endpoint = title === 'Itens' ? '/api/itens' : '/api/kits';
    const url = `http://localhost:8000${endpoint}`; // Ajuste para o URL da sua API

    try {
      const response = await fetch(url);
      const jsonData = await response.json();

      // Aqui, você pode aplicar lógica adicional baseada em 'timePeriod', se necessário.
      // Por exemplo, filtrar os dados baseado no período selecionado.
      setData(jsonData);
    } catch (error) {
      console.error('Falha ao buscar dados:', error);
      setData([]); // Limpa os dados em caso de erro.
    }
  };

  useEffect(() => {
    fetchData();
  }, [title, timePeriod]); // Rebusca os dados quando 'title' ou 'timePeriod' mudam.

  const handleTimePeriodChange = (event) => {
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
              <th>Nome</th>
              <th>Quantidade</th>
            </tr>
          </thead>
          <tbody>
            {data.map((item, index) => (
              <tr key={index}>
                <td>{item.nome}</td>
                {/* A quantidade é tratada diferentemente para itens e kits */}
                <td>{title === 'Itens' ? 'N/A' : item.itens.length}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TabelaLog;
