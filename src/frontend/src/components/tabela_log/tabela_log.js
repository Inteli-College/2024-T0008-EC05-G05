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
  const [timePeriod, setTimePeriod] = useState('dia'); // Padrão para 'dia', alinhado com os valores do menu suspenso

  // Mapeamento para corresponder ao estado interno aos parâmetros de período esperados pela API


  // Função fetchData memorizada para buscar dados na API
  const fetchData = useCallback(async () => {
    console.log("Buscando dados para", title, "com período", timePeriod);
    // Ajusta o endpoint com base no título
    const endpoint = title.toLowerCase() === 'itens' ? '/log/itens' : '/log/kits';
    // Acrescenta o período selecionado à URL
    const period = mapPeriod[timePeriod] || 'day';
    const url = `http://127.0.0.1:8080${endpoint}/${period}`;

    try {
      const response = await fetch(url);
      const jsonData = await response.json();
      setData(jsonData);
      console.log("Dados buscados:", jsonData);
    } catch (error) {
      console.error('Falha ao buscar dados:', error);
      setData([]); // Limpa os dados em caso de erro
    }
  }, [title, timePeriod]); // Dependências

  useEffect(() => {
    fetchData();
  }, [fetchData]); // A array de dependências agora inclui fetchData

  const handleTimePeriodChange = (event) => {
    console.log("Período selecionado:", event.target.value);
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
            <option value="mes">Mês</option>
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
