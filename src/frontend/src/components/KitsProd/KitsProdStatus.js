import React, { useState, useEffect } from 'react';
import './KitsProdStatus.css'; // Este arquivo conterá os estilos para o componente
import { IoMdTime } from "react-icons/io";
import { IoClose } from "react-icons/io5";

function  KitsProdStatus({ kitName, imageUrl, startTime, isFirst }) {
  const [elapsedTime, setElapsedTime] = useState('');


  useEffect(() => {

    // Função para calcular a diferença de tempo desde o início da produção
    const timeElapsed = () => {
      const now = new Date();
      const start = new Date(startTime);
      const difference = now.getTime() - start.getTime();

      // Converter a diferença de tempo para um formato legível (horas:minutos:segundos)
      const hours = Math.floor(difference / (1000 * 60 * 60));
      const minutes = Math.floor((difference / (1000 * 60)) % 60);
      const seconds = Math.floor((difference / 1000) % 60);

      setElapsedTime(`${hours}h ${minutes}m ${seconds}s`);
    };

    // Atualizar o tempo passado a cada segundo
    const interval = setInterval(timeElapsed, 1000);

    // Limpar o intervalo quando o componente for desmontado
    return () => clearInterval(interval);
  }, [startTime]);


  return (
    <div className="kit-production-status">
      <IoClose className="close-icon" />
      <div className="kit-photo">
        <img src={imageUrl} alt={`Kit ${kitName}`} />
      </div>
      <div className="kit-info">
        <h3>{kitName}</h3>
        <p>{isFirst ? `Tempo passado: ${elapsedTime}` : 'Na fila'}</p>
      </div>
      <div className='kits-date'>
        <p><IoMdTime /><b>Início: </b><p className='dateInfo'>{`${new Date(startTime).toLocaleString('pt-BR')}`}</p></p>
      </div>
    </div>
  );
}

export default KitsProdStatus;
