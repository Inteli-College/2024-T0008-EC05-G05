import React, { useState } from 'react';
import './Popup.css';

const ModalCreated = ({ isOpen, onRequestClose, placeholder, inputValue, onInputChange }) => {
  // State to manage items in the modal
  const [items, setItems] = useState([]);

  // Function to add item
  const addItem = () => {
    if (inputValue.trim() !== '') {
      // Make GET request using inputValue
      // Assume you have a function to make GET requests, replace 'fetchData' with your actual function
      fetchData(inputValue).then((data) => {
        // Update items state with the retrieved data
        setItems([...items, data]);
        // Clear input field
        onInputChange(''); // Clear input value in parent component
      }).catch(error => {
        console.error('Error fetching data:', error);
      });
    }
  };

  // Placeholder function for fetchData
  const fetchData = (inputValue) => {
    // Simulating a GET request with a timeout
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(inputValue); // Simulating that we receive the inputValue as data
      }, 1000); // Simulating a 1 second delay
    });
  };

  // Function to remove item by index
  const removeItem = (index) => {
    const updatedItems = [...items];
    updatedItems.splice(index, 1);
    setItems(updatedItems);
  };

  return (
    <div>
      {isOpen && (
        <div className="modal">
          <div className="modal-content">
            <header>Editar componente</header>
            <h4>Information </h4>
            <span className="close" onClick={onRequestClose}>&times;</span>
            <div>
              {/* Input field to add item */}
              <input
                type="text"
                placeholder={placeholder}
                value={inputValue}
                onChange={(e) => onInputChange(e.target.value)} // Update input value in parent component
              />
              {/* Button to add item */}
              <button onClick={addItem}>Add Item</button>
            </div>
            {/* Display items */}
            <ul>
              {items.map((item, index) => (
                <li key={index}>
                  {item} {/* Display retrieved data */}
                  <button onClick={() => removeItem(index)}>Remove</button>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};

export default ModalCreated;
