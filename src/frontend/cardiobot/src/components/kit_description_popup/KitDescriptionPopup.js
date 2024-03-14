import React, { useState, useEffect } from 'react';
import axios from 'axios';
import "./KitDescriptionPopup.css"

const Modal = ({ showModal, closeModal, kitId }) => {
  const [kitData, setKitData] = useState(null);

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
          {kitData && kitData.item_1 ? (
            <>
              <h3>Itens do Kit {kitData.id_kit} </h3>
              <ul>
                {kitData.item_1.map((item, index) => (
                  <li key={index}>Item {index + 1}: {item}</li>
                ))}
              </ul>
            </>
          ) : (
            <p>Loading...</p>
          )}
          <button onClick={closeModal}>Iniciar</button>
        </div>
      </div>
  );
};

export default Modal;
