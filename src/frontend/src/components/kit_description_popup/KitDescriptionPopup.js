import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./KitDescriptionPopup.css"

const Modal = ({ showModal, closeModal, kitId }) => {
  const [kitData, setKitData] = useState(null);

  const montarKit = async (kitCode) => {
    try {
      const response = await axios.get(`http://10.128.0.37:8800/montar_kit/?kit_code=${kitCode}`);
      console.log(response.data);
      // Lógica adicional aqui (e.g., atualizar o estado do componente)
    } catch (error) {
      if (error.response) {
        // A requisição foi feita e o servidor respondeu com um status code fora do range 2xx
        console.error("Erro na resposta do servidor:", error.response.data);
      } else if (error.request) {
        // A requisição foi feita mas não houve resposta
        console.error("Nenhuma resposta recebida:", error.request);
      } else {
        // Algum erro ocorreu ao montar a requisição
        console.error("Erro ao fazer a requisição:", error.message);
      }
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      try {
        if (kitId) {
          const response = await axios.get(`http://localhost:8000/posts/${kitId}`);
          setKitData(response.data);
          console.log(`Fetching data for kitId: ${kitId}`, response.data);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    if(showModal) {
      fetchData();
    }
  }, [showModal, kitId]);

  if (!showModal) return null;

  return (
    <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
          <h2>Descrição do Kit</h2>
          {kitData && kitData.ID ? (
            <>
              <h3>Itens do Kit {kitData.ID} </h3>
              <ul>
                {kitData.item_sku.map((item, index) => (
                  <li key={index}>Item {index + 1}: {item}</li>
                ))}
              </ul>
            </>
          ) : (
            <p>Loading...</p>
          )}
          <button onClick={() => montarKit(kitData.ID)}>Iniciar</button>
        </div>
      </div>
  );
};

export default Modal;
