import React, { useState, useEffect } from 'react';

const Modal = ({ showModal, closeModal, kitId }) => {
  const [kitData, setKitData] = useState(null);
  console.log("oiiiiii sou o kit ---->", kitId)

  useEffect(() => {
    // Fetch kit data based on kitId when showModal becomes true
    const fetchData = async () => {
      try {
        console.log("this is the ", kitId)
        // Ensure kitId is valid before making the request
        if (kitId) {
          // Make GET request using kitId
          // Replace the following line with your actual API request
          console.log(`Fetching data for kitId: ${kitId}`);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [showModal, kitId]); // Re-run effect when showModal or kitId changes

  if (!showModal) return null;

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={closeModal}>&times;</span>
        <h2>Descrição do Kit</h2>
        <p>${kitId}---- </p>
        <p>Modal content goes here.{kitData}</p>
        <button>Iniciar </button>
      </div>
    </div>
  );
};

export default Modal;
