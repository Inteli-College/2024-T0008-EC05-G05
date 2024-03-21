import React, { useState } from 'react';
import './Popup.css';

const ModalCreated = ({ isOpen, onRequestClose, title }) => {
  const [hasMedicine, setHasMedicine] = useState(false);
  const [quantity, setQuantity] = useState(0);

  const toggleMedicine = () => {
    setHasMedicine(!hasMedicine);
    // Reset quantity when toggling medicine
    setQuantity(0);
  };

  const incrementQuantity = () => {
    setQuantity(quantity + 1);
  };

  const decrementQuantity = () => {
    if (quantity > 0) {
      setQuantity(quantity - 1);
    }
  };

  return (
    <div>
      {isOpen && (
        <div className="modal">
          <div className="modal-content">
            <header>{title}</header>
            <span className="close" onClick={onRequestClose}>&times;</span>
            <div>
              {/* Button to toggle medicine */}
              <button onClick={toggleMedicine}>
                {hasMedicine ? 'Possui' : 'Não possui'}
              </button>
              {/* Quantity counter */}
              {hasMedicine && (
                <div>
                  <button onClick={decrementQuantity}>-</button>
                  <span>{quantity}</span>
                  <button onClick={incrementQuantity}>+</button>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default ModalCreated;
