import React from 'react';
import './Popup.css';

const ModalCreated = ({ isOpen, onRequestClose }) => {
  return (
    <div>
      {isOpen && (
        <div className="modal">
          <div className="modal-content">
            <h4>This is a test </h4>
            <span className="close" onClick={onRequestClose}>&times;</span>
            <p>Hello!</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default ModalCreated;
