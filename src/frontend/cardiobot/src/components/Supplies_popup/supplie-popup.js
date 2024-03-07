import React, { useState } from 'react';
import './Popup.css';

const Modal = () => {
  const [showModal, setShowModal] = useState(false);

  const openModal = () => {
    setShowModal(true);
  };

  const closeModal = () => {
    setShowModal(false);
  };

  return (
    <div>
      <button onClick={openModal}>Open Modal</button>
      {showModal && (
        <div className="modal">
          <div className="modal-content">
            <h4>This is a test </h4>
            <span className="close" onClick={closeModal}>&times;</span>
            <p>Hello!</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Modal;
