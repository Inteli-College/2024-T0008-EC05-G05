import React from 'react';
import './KitProd.css'; // Este arquivo conterá os estilos para o componente

function KitProd({ kitName, imageUrl, startTime }) {

  // Função para calcular a diferença de tempo desde o início da produção
  const timeElapsed = () => {
    const now = new Date();
    const start = new Date(startTime);
    const difference = now.getTime() - start.getTime();

    // Converter a diferença de tempo para um formato legível (horas:minutos:segundos)
    const hours = Math.floor(difference / (1000 * 60 * 60));
    const minutes = Math.floor((difference / (1000 * 60)) % 60);
    const seconds = Math.floor((difference / 1000) % 60);

    return `${hours}h ${minutes}m ${seconds}s`;
  };

  return (
    <div className="kit-production-status">
      <div className="kit-photo">
        <img src={imageUrl} alt={`Kit ${kitName}`} />
      </div>
      <div className="kit-info">
        <h3>{kitName}</h3>
        <p>{`Tempo passado: ${timeElapsed()}`}</p>
      </div>
    </div>
  );
}

export default KitProd;
