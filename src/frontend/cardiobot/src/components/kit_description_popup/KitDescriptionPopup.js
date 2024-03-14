// Modal.js
import React from 'react';

const Modal = ({ showModal, closeModal }) => {
  if (!showModal) return null;

  return (
    <div className="modal">
      <div className="modal-content">
        <span className="close" onClick={closeModal}>&times;</span>
        <h2>Descrição do Kit</h2>
        <p>Modal content goes here.</p>
        <button>Iniciar</button>
      </div>
    </div>
  );
};

export default Modal;
